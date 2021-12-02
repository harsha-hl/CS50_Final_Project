import os
import sys
from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash

from helpers import apology, login_required, rupee, name, cost

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
app.jinja_env.filters["cost"] = cost


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///Shoes.db")

@app.route("/", methods =["GET", "POST"])
def index():
    """Show homepage of website"""
    if request.method == "GET":
        return render_template("index.html")
    else:
        final_brand = None
        final_type = None
        shoe_type1 = None
        shoe_type2 = None
        shoe_brand2 = None
        shoe_type3 = None
        shoe_brand3 = None
        shoe_type1 = request.form.get("clicked_button1")
        shoe_type3 = request.form.get("clicked3")

        shoe_type2 = request.form.get("clicked2")
        if shoe_type2:
            shoe_brand2 = "Nike"
        elif shoe_type3:
            shoe_brand3 = "Adidas"


        if shoe_type1:
            final_type = shoe_type1
        elif shoe_type2:
            final_type = shoe_type2
        elif shoe_type3:
            final_type = shoe_type3


        if shoe_brand2:
            final_brand = shoe_brand2
        if shoe_brand3:
            final_brand = shoe_brand3

        if final_brand and final_type:
            shoes = db.execute("SELECT * FROM shoes WHERE type = ? AND brand = ?",final_type,final_brand)
        if final_brand and not final_type:
            shoes = db.execute("SELECT * FROM shoes WHERE brand = ?",final_brand)
        if final_type and not final_brand:
            shoes = db.execute("SELECT * FROM shoes WHERE type = ?",final_type)

        return render_template("products.html", shoes = shoes)



@app.route("/products", methods=["GET", "POST"])
def products():
    """Show products of website"""
    if request.method == "POST":
        data = {}    # empty dict to store data
        x = request.json['title']
        data['release_date'] = request.json['movie_release_date']

       #do whatever you want with the data here e.g look up in database or something
       # if you want to print to console

        print(x)
        print("\n\n\n\n\n\n\n")

        # then return something back to frontend on success
        shoes = db.execute("SELECT * FROM shoes;")
        return render_template("products.html", shoes = shoes)
        # this returns back received data and you should see it in browser console
        # because of the console.log() in the script.
        return jsonify(data)
    else:
        shoes = db.execute("SELECT * FROM shoes;")
        return render_template("products.html", shoes = shoes)
        

@app.route("/logout")
def logout():
    """Log user out"""

    #Forget any user_id
    session.clear()

    #Redirect user to login form
    return redirect("/")

@app.route("/productpage", methods=["GET", "POST"])
def productpage():
    if request.method == "POST":
        return render_template("productpage.html")
    else:
        print("\n\n\n\n\n\n\n")
        return render_template("productpage.html", path = "/static/images/shoes/adidasSneakers/8679Dame_7_EXTPLY_Shoes_White.jpg")


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

