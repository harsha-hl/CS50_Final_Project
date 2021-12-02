from cs50 import SQL
import random
import os
from string import capwords

db = SQL("sqlite:///shoes.db")
Db = SQL("sqlite:///Shoes.db")

directory = '/home/harsha/C/cs50/CS50_Final_Project/static/images/shoes/nikeSports'
a = "/static/images/shoes/nikeSports/8777tiempo-legend-9-club-mg-multi-ground-football-boot.jpeg"
a = (a.rpartition('/')[2]).rpartition('.')[0]
b=""
for i in a:
    if i == '-' or i =='_':
        b = b+" "
    else:
        b = b+i
if b[4].isdigit():
    print(capwords(b[5:]))
else:
    print(capwords(b[4:]))

#a = (a.rpartition('/')[2]).rpartition('.')[0]
#if a[4].isdigit():
 #   print(int(a[0:5]))
#else:
 #   print(int(a[0:4]))

#for filename in os.listdir(directory):
 #   if filename.endswith(".png") or filename.endswith(".jpg") or filename.endswith(".jpeg"):
  #      filename = "/static/images/shoes/nikeSports/" + filename
   #     print(filename)
    #    Db.execute("INSERT INTO shoes (name, type, brand) VALUES(?, ?, ?)", filename, "Sports", "Nike")

#shoes = db.execute("SELECT * FROM shoes WHERE brand=? AND type=? ;","Adidas","Sneakers")
