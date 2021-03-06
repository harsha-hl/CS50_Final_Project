import os
import requests
import urllib.parse

from string import capwords
from flask import redirect, render_template, request, session
from functools import wraps


def apology(message, code=400):
    """Render message as an apology to user."""
    def escape(s):
        """
        Escape special characters.

        https://github.com/jacebrowning/memegen#special-characters
        """
        for old, new in [("-", "--"), (" ", "-"), ("_", "__"), ("?", "~q"),
                         ("%", "~p"), ("#", "~h"), ("/", "~s"), ("\"", "''")]:
            s = s.replace(old, new)
        return s
    return render_template("apology.html", top=code, bottom=escape(message)), code


def login_required(f):
    """
    Decorate routes to require login.

    https://flask.palletsprojects.com/en/1.1.x/patterns/viewdecorators/
    """
    @wraps(f)
    def decorated_function(*args, **kwargs):
        if session.get("user_id") is None:
            return redirect("/login")
        return f(*args, **kwargs)
    return decorated_function

def rupee(value):
    """Format value as Rupee."""
    return f"\u20B9 {float(value):,.2f}"

def name(a):
    a = (a.rpartition('/')[2]).rpartition('.')[0]
    b=""
    for i in a:
        if i == '-' or i =='_':
            b = b+" "
        else:
            b = b+i
    if b[4].isdigit():
        return(capwords(b[5:]))
    else:
        return(capwords(b[4:]))

def cost(a):
    a = (a.rpartition('/')[2]).rpartition('.')[0]
    if a[4].isdigit():
        return(int(a[0:5]))
    else:
        return(int(a[0:4]))