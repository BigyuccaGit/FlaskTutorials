from flask import Flask, redirect, url_for

app = Flask(__name__)

# Defining the home page of our site
@app.route("/")  # this sets the route to this page
def home():
	return "Hello! this is the main page <h1>HELLO</h1>"  # some basic inline html#

# Dynamic URL
@app.route("/<name>")
def user(name):
    return f"Hello {name}!"

# Redirect
@app.route("/admin")
def admin():
	return redirect(url_for("home")) # Note, uses name of function, not route

if __name__ == "__main__":
    app.run()