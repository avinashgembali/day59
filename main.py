from flask import Flask, render_template
import requests

app = Flask(__name__)
response = requests.get(url="https://api.npoint.io/20e64eeb358daea5fca7")
blogs = response.json() # list of blogs containing dictionary with id body title subtitle image


@app.route("/")
def home():
    return render_template("index.html", blogs=blogs)


@app.route("/about")
def about():
    return render_template("about.html")


@app.route("/contact")
def contact():
    return render_template("contact.html")


@app.route("/post/<int:index>")
def show_post(index):
    requested_post = None
    for blog_post in blogs:
        if blog_post["id"] == index:
            requested_post = blog_post
    return render_template("post.html", post=requested_post)


if __name__ == "__main__":
    app.run(debug=True)


