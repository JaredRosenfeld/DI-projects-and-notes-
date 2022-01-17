from app import db


class Book(db.Model):

    book_id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(64))
    author = db.Column(db.String(64))
    price = db.Column(db.Float)

    def __repr__(self):
        return f'<Book: {self.title}>'
Book55= Book(book_id = 55,title = 'Book55', author = '123', price = 15)
Book44 = Book(book_id = 44, title = 'Book44',author ='123', price =20)
# db.create_all()
# db.session.add(Book55)
# db.session.add(Book44)
# db.session.commit()
# db.delete(Book4)
# db.session.delete(Book4)
# db.session.commit()
# db.delete(Book4)
# db.drop_all()
# db.session.commit()
# u = db.session.get(Book4, 1)
# db.session.delete(u)
# db.session.commit()
#
# db.drop_all()
# db.session.commit()

# db.create_all()
# db.session.delete(Book55)
# db.session.commit()

# db.session.query(Book).filter_by(book_id = 55).delete()
# db.session.commit()
# db.query.all