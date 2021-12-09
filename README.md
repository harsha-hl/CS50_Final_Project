# *H&A* Shopping Web Application

## This is my final project for Harvard's CS50x : Introduction to Computer Science course.
 
![Homepage](static/images/1.jpg)

#### Video Demo : <URL HERE>

## Introduction
  This *H&A* Shopping website is a web based application that is designed using the [Flask](https://flask.palletsprojects.com/en/2.0.x/) framework. It basically mimics a shopping site(inspired by *h&m* fashion) where users can register, login, and buy fashion products(shoes in this case). The application follows a **Model - View - Controller** design pattern having components developed using Flask (ie Python for back-end), SQL database to act as the model and finally the front-end developed using html css and javascript with the help of frameworks like Bootsrap 4 and more.
  
## Model
  For the model, I have used a Structured Query Language or SQL database named ```Shoes.db```. It is a relational database management system consisting of 4 tables namely shoes, users, cart and orders. These tables and their respective fields can be viewed using the command ```.schema``` under sqlite3 (an example). Every user and shoe being unique have their own ids which act as primary keys and these keys are referenced to by the foreign keys in tables cart and orders so as to facilitate easy data management across tables.
  
 ![Homepage](static/images/1.jpg)
 ![Homepage](static/images/1.jpg)

## View
  The above images will give you a glimpse of the application / site which a user will be exposed to. Most of the components, hover effects, transisitons and gradients have been implemented using plain css and javascript with html combining the two to make the webpages. Also certain features like navigation bars and alerts have been designed using Bootstrap 4. The user will be able to view products by category and brand, add them to cart, review the prices, select the size and number of pairs they wish to order and also mimic a payment showing the completion of transaction. They will also be able to view their cart items and order history at any given moment. Each of the many webpages present extend a ```layout.html``` file present in the templates folder. This is made possible by using [Jinja](https://jinja.palletsprojects.com/en/3.0.x/), a fast and expressive, extensible templating engine. The images and logos used across the website have been stored in the static folder which also includes other static files such as a video, ```styles.css``` and ```scripts.js``` .
  
## Controller
Python language has been used for implementing the backend. The files app.py and helpers.py are responsible for the maintenance of the site. ```Shoes.db``` has been linked to this python code so as to dynamically read or update the database for displaying information on the site. The user will not be able to add items to cart or order them without signing in with a username and password. If the user doesn't have an account already, they can easily create one in the signup page as shown below. Care has been taken so as to prevent users from performing SQL injection attacks and are also prevented from entering invalid data at any of the fields on the site so as to make it reliable. The images of signup and login page can be seen as follows..
  
  SIGNUP LOGIN
   ![Homepage](static/images/1.jpg)
  
 ## More on Flask
  As mentioned earlier, the framework implies the use of a certain structure of directory / file listing as shown below:
1. ```static/``` contains all the static files like css, javascript files, images and videos.
2. ```templates/``` contains all the html files used to implement the webpages with a ```layout.html``` file acting as the base for other files.
3. ```Shoes.db``` is the database used to store all data including shoe and user information.
4. ```app.py``` and ```helpers.py``` are the files handling the server and responding to get and post requests made to it.
5. ```requirements.txt``` is a text file which contains the names of additional libraries / software that may be required to host and run the application.  

  By default, ```flask run``` command starts flask's built in webserver and runs it on localhost. Using ```flask run --host=0.0.0.0``` changes it to run on all your machine's IP addresses.
![Homepage](static/images/1.jpg)
![Homepage](static/images/1.jpg)
![Homepage](static/images/1.jpg)
  
  ## About CS50
  Building this application wouldn't be possible without the help and guidance offered by the course's instructors David and Brian. From all-nighter Tideman to fascinating Filters and Fiftyville, the course has been truly amazing with its collection of problem sets and labs. I have enjoyed being a part of cs50 and would certainly recommend it to anyone interested in the domain of computer science.
  
  This was cs50 !!!
