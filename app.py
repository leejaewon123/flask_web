from flask import Flask , render_template
from data import Articles

app = Flask(__name__)

app.debug = True

#라우팅 파일을 만드는 방법
@app.route('/', methods=['GET'])
def index():
  # return "Hello world"
  return render_template("index.html", date="kim")

@app.route('/about')
def about():
  return render_template("about.html", hello = "gary kim")

@app.route('/articles')
def articleS():
  articles = Articles()
  print(articles)
  return render_template("articles.html", articles = articles)

@app.route('/article/<int:id>')
def article(id):
  articles = Articles()
  article = articles[id-1]
  print(articles[id-1])
  return render_template("article.html" , article = article)

if __name__ == '__main__':
    app.run()