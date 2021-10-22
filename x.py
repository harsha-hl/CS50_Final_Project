import os
directory = '/home/harsha/C/cs50/CS50_Final_Project/static/images/shoes/crocs'

for filename in os.listdir(directory):
    if filename.endswith(".png"):
    	print(filename)
