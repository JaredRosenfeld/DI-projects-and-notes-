from app import db


class Book(db.Model):
	book_id = db.Column(db.Integer, primary_key=True)
	title = db.Column(db.String(64))
	price = db.Column(db.Float)

	author_id = db.Column(db.Integer, db.ForeignKey('author.author_id'))

	def __repr__(self):
		return f'<Book: {self.title}>'


class Author(db.Model):
	author_id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(64))

	books = db.relationship('Book', backref='author', lazy='dynamic')

	def __repr__(self):
		return f'<Author: {self.name}>'
