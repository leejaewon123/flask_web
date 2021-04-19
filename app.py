from flask import Flask , render_template


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
def article():
    return render_template("articles.html", hello = "gary kim")

if __name__ == '__main__':
    app.run()