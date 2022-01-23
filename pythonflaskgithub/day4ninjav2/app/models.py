import binary as binary
import enum
import numpy as np
from app import db, s1, Base
from sqlalchemy import *
from sqlalchemy.orm import relationship

class Todolist(db.Model):
    __tablename__ = 'Todolist'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    todo = db.Column(db.String(500))
    check = db.Column(db.Boolean(),default = False)

    def __repr__(self):
        return f'<todo: {self.todo}>'

    def save(self):
        db.session.add(self)
        db.session.commit()



