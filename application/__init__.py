from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql
import os



#Create a Flask Instance
app = Flask(__name__)

#SQLAlchemy Database Configurated
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///students.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = getenv('secretkey')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

#Initialise the database
db = SQLAlchemy(app)


import application.models
import application.forms
import application.routes