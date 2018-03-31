from flask import Flask, render_template, url_for, request
from flask.ext.sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLAlCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres123@localhost/articles'
db = SQLAlchemy(app)

class loadArticle(db.Model):
    __tablename__="data"
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(15), unique=True)
    password = db.Column(db.String(20))
    email = db.Column(db.String(50), unique=True)
    title = db.Column(db.String(30), unique=True)
    article = db.Column(db.String(120))
#    created_at = db.Column(db.DateTime, default=datetime.now())

# def __init__(self,username,password,email,title,article):
#     self.username=username
#     self.password=password
#     self.email=email
#     self.title=title
#     self.article=article

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/articles')
def articles():
    return render_template('articles.html')

@app.route('/projects')
def projects():
    return render_template('projects.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/loadarticle')
def loadarticle():
    return render_template('load-article.html')

@app.route('/write', methods=['POST'])
def write_to_database():
    if request.method == 'POST':
        title = request.form["article_title"]
        article = request.form["article_body"]
        if (db.session.query(loadArticle).filter(loadArticle.title==title).count == 0):
            load_article = loadArticle(title,article)
            db.session.add(load_article)
            db.commit()
            return render_template("articles.html")
        pass
    return render_template('write-article.html')

if __name__=='__main__':
    app.run(debug=True)
