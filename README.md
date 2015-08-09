LuizaLabs Challenge
===================

#### Objective

Create an API that collects user information from Facebook and provides those information through an service.

#### How to run

Create an folder for this project and navigate into the folder
```
$ mkdir labs-api && cd labs-api
```
Now you can:

Clone this repository inside the folder that you just created
```
$ git clone https://github.com/guilherme-toti/desafio-luizalabs.git .
```
Or [download this repository](https://github.com/guilherme-toti/desafio-luizalabs/archive/master.zip) as ZIP file and extract it into the folder you created.

Now if you are using virtualenv, create a virtualenv and activate it, if you don't, just go to next step
```
$ virtualenv venv && source venv/bin/activate
```
Once you are inside virtualenv, you need to install the dependences:
```
$ pip install -r dependences.txt
```
When pip finish, you can navigate to "api" folder
```
$ cd api
```
And just run
```
$ python main.py
```
Now your API is running on: http://localhost:8888

#### Structure

This is the structure of files and folders of this project
```
.
+-- api
|   +-- handlers
|   |   +-- person.py - All request types for /person
|   +-- helpers
|   |   +-- facebook.py - Helper to get user information from Facebook Graph API
|   +-- logs
|   |   +-- application.log - File with all application logs
|   +-- sqlite - Folder with the sqlite database
|   +-- __init__.py
|   +-- database.py - Database configs and connection
|   +-- main.py - Here is the routes and this is the file that you need to run with 'python' command
|   +-- models.py - SQLAlchemy user model
+-- .gitignore
+-- README.md
+-- dependences.txt - The dependences of this project it's listed here
```

