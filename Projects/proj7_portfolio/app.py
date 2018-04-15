from flask import Flask, render_template, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, DateTime
import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/articles'
db = SQLAlchemy(app)

class loadArticle(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer, primary_key=True)
    user_name = db.Column(db.String(20))
    title = db.Column(db.String(30), unique=True)
    article = db.Column(db.String(1000))
    date_posted = db.Column(db.Date(), default=datetime.datetime.now)

    def __init__(self,user_name,title,article,date):
        self.user_name = user_name
        self.title = title
        self.article = article
        self.date = date

class loadUserData(db.Model):
    __tablename__="userdata"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/articles')
def articles():
    alldata = loadArticle.query.all()
    return render_template('articles.html', alldata = alldata)

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loadarticle/<article_id>')
def loadarticle(article_id):
    loadpost = loadArticle.query.filter_by(id=article_id).all()
    # articles = loadArticle.query.article
    return render_template('load-article.html', loadpost = loadpost)

@app.route('/write', methods=['GET','POST'])
def write_to_database():
    if request.method == 'POST':
        name = request.form["user_name"]
        title = request.form["article_title"]
        article = request.form["article_body"]
        date = datetime.datetime.now() #request.form["date_posted"]
        if db.session.query(loadArticle).filter(loadArticle.title==title).count() == 0:
            store_article = loadArticle(name,title,article,date)
            db.session.add(store_article)
            db.session.commit()
        return '<h1> New article has been created.</h1>'
    return render_template('write-article.html')

if __name__=='__main__':
    app.run(debug=True)
