from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import random
import os

# Flask Object
app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('set FLASK_APP=run.py')


# Database Connection
db_info = {'host': 'localhost',
           'database': 'bookstore',
           'psw': '123',
           'user': 'postgres',
           'port': ''}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# Database Representation
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import models, routes

