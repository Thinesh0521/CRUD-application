from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from os import getenv
import pymysql
import os

#SQLAlchemy Database Configurated
app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:///data.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
#app.config['SECRET_KEY'] = getenv('secretkey')
SECRET_KEY = os.urandom(32)
app.config['SECRET_KEY'] = SECRET_KEY

db = SQLAlchemy(app)

import application.models
import application.forms
import application.routes