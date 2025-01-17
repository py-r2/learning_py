from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField
from wtforms.validators import InputRequired, Email, Length
from flask_bootstrap import Bootstrap
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI']='postgresql://postgres:postgres123@localhost/portfolio_website'
app.config['SECRET_KEY']='thisisnotthe right secret phrase'
bootstrap = Bootstrap(app)
db = SQLAlchemy(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

#define database model by inheriting from UserMixin user class properties and methods
class storeUserData(UserMixin, db.Model):
    __tablename__="userdata"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(80))
    email = db.Column(db.String(50), unique=True)
    company = db.Column(db.String(120))

#define user login form
class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=3, max=30)])
    remember = BooleanField('remember me')

#define user registration form
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email')])
    username = StringField('username', validators=[InputRequired(), Length(min=3, max=15)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=3, max=30)])
    company = StringField('company', validators=[InputRequired()])

@login_manager.user_loader
def load_user(user_id):
    return storeUserData.query.get(int(user_id))

@app.route('/')
def index():
    return render_template('index.html')

'''verifying password match with module login_user of flask_login library and
in case of success redirect to a bootstrap dashboard page'''

@app.route('/login', methods=['GET','POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = storeUserData.query.filter_by(username=form.username.data).first()
        if user:
            if check_password_hash(user.password, form.password.data):
                login_user(user,remember=form.remember.data)
                return redirect(url_for('dashboard'))
        return '<h1>Invalid username or password.</h1>'
    return render_template('login.html', form=form)

'''adding new_user in to database with a generated hash password
(used werkzeug.security library) so you don't see the password in clear, just in
case someone queries the database'''

@app.route('/signup', methods=['GET','POST'])
def signup():
    form = RegisterForm()
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = storeUserData(username=form.username.data, password=hashed_password,
        email=form.email.data, company=form.company.data)
        db.session.add(new_user)
        db.session.commit()
        return '<h1> New user has been created.</h1>'
    return render_template('signup.html', form=form)

@app.route("/logout")
@login_required #using module login_required to verify if you are logged in or not
def logout():
    logout_user()
    return redirect(url_for('index'))

@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

if __name__ == '__main__':
    app.run(debug=True)
