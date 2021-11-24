import os

from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, rupee, name

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True


# Ensure responses aren't cached
@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Custom filter
app.jinja_env.filters["rupee"] = rupee
app.jinja_env.filters["name"] = name


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///shoes.db")

@app.route("/")
def index():
    """Show homepage of website"""
    return render_template("index.html")


@app.route("/logout")
def logout():
    """Log user out"""

    #Forget any user_id
    session.clear()

    #Redirect user to login form
    return redirect("/")


@app.route("/signup", methods = ["GET", "POST"])
def signup():
    """Register user"""

    if request.method == "GET":
        print("HIIIIIIIIIIIIIIIIIII")
        return render_template("signup.html")

    else:
        username = request.form.get("username")
        #if username already taken then use return render_template("signup.html",check = 1)
        return redirect("/")



@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
        #Password doesnt match use return render_template("login.html",check = 2)
        #Invalid username use return render_template("login.html",check = 1)

