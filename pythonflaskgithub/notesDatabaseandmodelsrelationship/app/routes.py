from app import app, db
from app.models import Book, Author
from app.forms import AddForm
from flask import redirect, render_template


@app.route('/')
def index():
	books = Book.query.all()
	return render_template('index.html', books=books)


@app.route('/add', methods=['GET', 'POST'])
def addbook():
	form = AddForm()

	if form.validate_on_submit():
		title = form.title.data
		author_name = form.author.data
		price = form.price.data

		get_all_authors_name_from_db = [aut.name.lower() for aut in Author.query.all()]

		if author_name.lower() not in get_all_authors_name_from_db:
			# creating new author
			author = Author(name=author_name)
			db.session.add(author)
		else:
			# get existing author from db
			author = Author.query.filter_by(name=author_name).first()

		newbook = Book(title=title, author=author, price=price)
		db.session.add(newbook)
		db.session.commit()
		return redirect('/')
	return render_template('addbook.html', form=form)
