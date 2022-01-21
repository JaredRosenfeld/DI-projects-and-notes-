import binary as binary
import enum
import numpy as np
from app import db, s1, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship


class News(db.Model):
    __tablename__ = 'news'

    news_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(5000))
    description = db.Column(db.String(50000))
    source = db.Column(db.String(50000))

    def __repr__(self):
        return f'<Title: {self.title}>'


class Users(db.Model):
    __tablename__ = 'users'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    user_name = db.Column(db.String(55), index=True, unique=True)
    age = db.Column(db.Integer)
    pets = db.relationship('Pets', backref='users', lazy='dynamic')


class Pets(db.Model):
    __tablename__ = 'pets'
    pet_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    pet_name = db.Column(db.String(64), index=True)
    pet_age = db.Column(db.Integer)
    owner = db.Column(db.String(55), db.ForeignKey('users.user_name'))


user1 = Users(user_name='Jared', age=26)
user2 = Users(user_name='Jamie', age=64)
pets1 = Pets(pet_name='Mooki', pet_age=5, owner=user1.user_name)
pets2 = Pets(pet_name='Cody', pet_age=17, owner=user1.user_name)
pets3 = Pets(pet_name='Aviv', pet_age=8, owner=user2.user_name)

# db.create_all()
# News1 = News(title = 'Boy Trapped in Well',description = 'There is a little boy in a well', source = 'Alex Jones')
# db.session.add(News1)
# db.session.delete(News1)
# delete_this = News.query.filter_by(news_id=2).first()
# db.session.delete(delete_this)
# db.session.commit()
# db.drop_all()
#
# db.session.add(user1)
# db.session.add(user2)
# db.session.add(pets1)
# db.session.add(pets2)
# db.session.add(pets3)
# db.session.commit()

# >psql user=postgres
# pwd: 123
