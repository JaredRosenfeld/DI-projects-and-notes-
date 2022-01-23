from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from sqlalchemy.ext.declarative import declarative_base
from flask_migrate import Migrate
import random
import os

# Flask Object
from sqlalchemy.orm import sessionmaker

app = Flask(__name__)
app.config['SECRET_KEY'] = random._urandom(56)
app.config['DEBUG'] = True
os.system('set FLASK_APP=main.py')


# Database Connection
db_info = {'host': 'localhost',
           'database': 'Schedule1',
           'psw': '123',
           'user': 'postgres',
           'port': ''}
app.config[
    'SQLALCHEMY_DATABASE_URI'] = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
engine1 = f"postgresql://{db_info['user']}:{db_info['psw']}@{db_info['host']}/{db_info['database']}"
# Database Representation
Base = declarative_base()
db = SQLAlchemy(app)
migrate = Migrate(app, db)
sessionmaker(bind=db)()
s1 = sessionmaker(bind=db)()
# engine = create_engine(engine1)
# create_database(engine.url)
# db.create_all()
# db.session.commit()
from app import models, routes