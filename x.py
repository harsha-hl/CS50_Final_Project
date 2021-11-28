from cs50 import SQL
import random
import os

db = SQL("sqlite:///shoes.db")

directory = '/home/harsha/C/cs50/CS50_Final_Project/static/images/shoes/nikeSports'

for filename in os.listdir(directory):
    if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
        filename = "/static/images/shoes/nikeSports/" + filename
        db.execute("INSERT INTO shoes (name, type, brand, cost) VALUES(?, ?, ?, ?)", filename, "Sports", "Nike", float(random.randrange(4000,18000)))