import os
import sys
import random
from cs50 import SQL
from datetime import datetime
from flask import Flask, flash, redirect, render_template, request, session, jsonify
from flask_session import Session
from tempfile import mkdtemp
from werkzeug.exceptions import default_exceptions, HTTPException, InternalServerError
from werkzeug.security import check_password_hash, generate_password_hash
from helpers import apology, login_required, rupee, name, cost
from datetime import datetime


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
        count = 0
        final_brand = None
        final_type = None
        shoe_type1 = None
        shoe_type2 = None
        shoe_brand2 = None
        shoe_type3 = None
        shoe_brand3 = None
        jump = None
        shoe_type1 = request.form.get("clicked_button1")
        shoe_type3 = request.form.get("clicked3")
        shoe_type2 = request.form.get("clicked2")
        jump =  request.form.get("jump")

        shoead = db.execute("SELECT * FROM shoes WHERE type != ?","Crocs")
        countad = db.execute("SELECT COUNT(name) FROM shoes WHERE type != ?","Crocs")

        if jump:
            return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = countad[0]["COUNT(name)"])

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

        if shoe_type2 == "Nike":
            final_type = None
            final_brand = "Nike"

        elif shoe_type2 == "Adidas":
            final_type = None
            final_brand = "Adidas"

        

        if final_brand and final_type:
            shoes = db.execute("SELECT * FROM shoes WHERE type = ? AND brand = ?",final_type,final_brand)
            count = db.execute("SELECT COUNT(name) FROM shoes WHERE type = ? AND brand = ?",final_type,final_brand)

        if final_brand and not final_type:
            shoes = db.execute("SELECT * FROM shoes WHERE brand = ?",final_brand)
            count = db.execute("SELECT COUNT(name) FROM shoes WHERE brand = ?",final_brand)

        if final_type and not final_brand:
            shoes = db.execute("SELECT * FROM shoes WHERE type = ?",final_type)
            count = db.execute("SELECT COUNT(name) FROM shoes WHERE type = ?",final_type)

        return render_template("products.html", shoes = shoes, count = count[0]["COUNT(name)"], shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]))


@app.route("/logout")
def logout():
    """Log user out"""

    #Forget any user_id
    session.clear()

    #Redirect user to login form
    return redirect("/")


@app.route("/productpage", methods=["GET", "POST"])
@login_required
def productpage():
    if request.method == "POST":
        atoc = request.form.get("atoc")
        bn = request.form.get("bn")
        size  = int(request.form.get("size"))
        qnty = int(request.form.get("qnty"))
        shoead = db.execute("SELECT * FROM shoes WHERE type != ?","Crocs")
        countad = db.execute("SELECT COUNT(name) FROM shoes WHERE type != ?","Crocs")
        if atoc:
            rows = db.execute("SELECT * FROM shoes WHERE name = ?", atoc)
            if rows[0]["qnty"] == 0:
                return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]), check = 2)
            
            elif qnty > rows[0]["qnty"]:
                return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]), check = 3)
            
            else:
                rows[0]["qnty"] = rows[0]["qnty"] - qnty
                sum = cost(atoc) * qnty
                db.execute("UPDATE shoes SET qnty = ? WHERE name = ?", rows[0]["qnty"], atoc)
                rows1 = db.execute("SELECT * FROM cart WHERE u_id = ? AND shoe_id = ? AND size = ?", session["user_id"], rows[0]["s_id"], size)
                if len(rows1) != 0:
                    rows1[0]["num"] = rows1[0]["num"] + qnty
                    rows1[0]["sum"] = rows1[0]["sum"] + sum
                    db.execute("UPDATE cart SET num = ?, sum = ? WHERE u_id = ? AND shoe_id = ? AND size = ?", rows1[0]["num"], rows1[0]["sum"], session["user_id"], rows[0]["s_id"], size)
                else:
                    db.execute("INSERT INTO cart (u_id, shoe_id, num, size, sname, sum) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], rows[0]["s_id"], qnty, size, atoc, sum)
                return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]), check = 1)
        else:
            rows = db.execute("SELECT * FROM shoes WHERE name = ?", bn)
            if rows[0]["qnty"] == 0:
                return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]), check = 2)
            
            elif qnty > rows[0]["qnty"]:
                return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]), check = 3)
            
            else:
                sum = cost(bn) * qnty
                rows1 = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
                if rows1[0]["cash"] < sum:
                    return render_template("productpage.html", shoead = shoead, rando = random.randint(5,9), countad = int(countad[0]["COUNT(name)"]), check = 4)
                rows1[0]["cash"] = rows1[0]["cash"] - sum
                db.execute("UPDATE users SET cash = ? WHERE id = ?", rows1[0]["cash"], session["user_id"])
                db.execute("INSERT INTO orders (user_id, shoe_name, s_num, size, bill, time) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], bn, qnty, size, sum,  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                orders = db.execute("SELECT * FROM orders WHERE user_id = ?", session["user_id"])
                cart = db.execute("SELECT * FROM cart WHERE u_id = ?", session["user_id"])
                total = db.execute("SELECT SUM(sum) FROM cart WHERE u_id = ?", session["user_id"])
                count = db.execute("SELECT SUM(num) FROM cart WHERE u_id = ?", session["user_id"])
                if not total[0]["SUM(sum)"]:
                    return render_template("cartorders.html", orders = orders, cart = cart, check = 4, total = 0, count = 0, balance = rows1[0]["cash"] )
                else:
                    return render_template("cartorders.html", orders = orders, cart = cart, check = 4, total = int(total[0]["SUM(sum)"]), count = int(count[0]["SUM(num)"]), balance = rows1[0]["cash"] )
    else:
        return render_template("productpage.html")

@app.route("/cartorders", methods=["GET", "POST"])
@login_required
def cartorders():
    orders = db.execute("SELECT * FROM orders WHERE user_id = ?", session["user_id"])
    cart = db.execute("SELECT * FROM cart WHERE u_id = ?", session["user_id"])
    row = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
    total = db.execute("SELECT SUM(sum) FROM cart WHERE u_id = ?", session["user_id"])
    count = db.execute("SELECT SUM(num) FROM cart WHERE u_id = ?", session["user_id"])
    if request.method == "GET":
        if total[0]["SUM(sum)"]:
            return render_template("cartorders.html", orders = orders, cart = cart, check = 0, total = int(total[0]["SUM(sum)"]), count = int(count[0]["SUM(num)"]), balance = row[0]["cash"])
        else: 
            return render_template("cartorders.html", orders = orders, cart = cart, check = 0, total = 0, count = 0, balance = row[0]["cash"])

    else:
        clear = request.form.get("clear")
        shoe_del = request.form.get("remove")
        buy = request.form.get("buy")
        add = request.form.get("add")
        amt = request.form.get("amt")
        if amt:
            amt = int(amt)

        if clear:
            db.execute("DELETE FROM cart WHERE u_id = ?", session["user_id"])
            cart = db.execute("SELECT * FROM cart WHERE u_id = ?", session["user_id"])
            return render_template("cartorders.html", orders = orders, cart = cart, check = 1, total = 0, count = 0, balance = row[0]["cash"])
        elif buy:
            total = db.execute("SELECT SUM(sum) FROM cart WHERE u_id = ?", session["user_id"])
            rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])

            if not total[0]["SUM(sum)"]:
                return render_template("cartorders.html", orders = orders, cart = cart, check = 2, total = 0, count = 0, balance = row[0]["cash"])

            elif int(total[0]["SUM(sum)"]) > rows[0]["cash"]:
                return render_template("cartorders.html", orders = orders, cart = cart, check = 3, total = int(total[0]["SUM(sum)"]), count = int(count[0]["SUM(num)"]), balance = rows[0]["cash"])
            else:
                cart1 = cart
                rows[0]["cash"] = rows[0]["cash"] - int(total[0]["SUM(sum)"])
                db.execute("UPDATE users SET cash = ? WHERE id = ?", rows[0]["cash"], session["user_id"])
                for shoe in cart1:
                    db.execute("INSERT INTO orders (user_id, shoe_name, s_num, size, bill, time) VALUES(?, ?, ?, ?, ?, ?)", session["user_id"], shoe["sname"], shoe["num"], shoe["size"], shoe["sum"],  datetime.now().strftime('%Y-%m-%d %H:%M:%S'))
                    db.execute("DELETE FROM cart WHERE u_id = ? AND shoe_id = ? AND size = ?", session["user_id"], shoe["shoe_id"], shoe["size"])
                orders = db.execute("SELECT * FROM orders WHERE user_id = ?", session["user_id"])
                cart = db.execute("SELECT * FROM cart WHERE u_id = ?", session["user_id"])
                return render_template("cartorders.html", orders = orders, cart = cart, check = 4,total = 0, count = 0, balance = rows[0]["cash"])
        elif add:
            rows = db.execute("SELECT * FROM users WHERE id = ?", session["user_id"])
            rows[0]["cash"] = rows[0]["cash"] + amt
            db.execute("UPDATE users SET cash = ? WHERE id = ?", rows[0]["cash"], session["user_id"])
            return render_template("cartorders.html", orders = orders, cart = cart, check = 5, total = int(total[0]["SUM(sum)"]), count = int(count[0]["SUM(num)"]), balance = rows[0]["cash"])
        
        elif shoe_del:
            db.execute("DELETE FROM cart WHERE u_id = ? AND shoe_id = ?", session["user_id"], shoe_del)
            cart = db.execute("SELECT * FROM cart WHERE u_id = ?", session["user_id"])
            total = db.execute("SELECT SUM(sum) FROM cart WHERE u_id = ?", session["user_id"])
            count = db.execute("SELECT SUM(num) FROM cart WHERE u_id = ?", session["user_id"])
            if not total[0]["SUM(sum)"]:
                return render_template("cartorders.html", orders = orders, cart = cart, check = 6, total = 0, count = 0, balance = row[0]["cash"])
            else:
                return render_template("cartorders.html", orders = orders, cart = cart, check = 6, total = int(total[0]["SUM(sum)"]), count = int(count[0]["SUM(num)"]), balance = row[0]["cash"])

@app.route("/signup", methods = ["GET", "POST"])
def signup():
    """Register user"""

    if request.method == "GET":
        return render_template("signup.html")

    else:
        username = request.form.get("username")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 0:
            return render_template("signup.html",check = 1)
        password = request.form.get("password")
        db.execute("INSERT INTO users (username, hash) VALUES(?, ?)", username, generate_password_hash(password))
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        session["user_id"] = rows[0]["id"]
        return redirect("/")


@app.route("/login", methods=["GET", "POST"])
def login():
    """Log user in"""

    # Forget any user_id
    session.clear()

    # User reached route via POST (as by submitting a form via POST)
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        rows = db.execute("SELECT * FROM users WHERE username = ?", username)
        if len(rows) != 1:
            return render_template("login.html", check = 1)

        if not check_password_hash(rows[0]["hash"],password):
            return render_template("login.html", check = 2)

        session["user_id"] = rows[0]["id"]

        # Redirect user to home page
        return redirect("/")

    # User reached route via GET (as by clicking a link or via redirect)
    else:
        return render_template("login.html")
