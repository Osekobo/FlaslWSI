from flask import Flask, redirect, url_for, render_template

app = Flask(__name__)

@app.route("/")
def landing():
  return "Hello! this is the landing page"

@app.route("/home")
def home():
  return render_template("base.html", content=["tim", "joe", "bill"])

if __name__ == "__main__":
  app.run()