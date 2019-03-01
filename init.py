from flask import Flask , render_template

app = Flask(__name__)

@app.route("/")
def hello():
	return render_template("index.html")
@app.route("/post")
def post():
	return render_template("post.html")

@app.route("/<home>")
def home_page(home):
	return render_template("personal_page.html",nick_name = home)

@app.route("/home_post")
def home_post():
	return render_template("poster.html")

if __name__ == "__main__":
	app.run(host="localhost",port=8080)

