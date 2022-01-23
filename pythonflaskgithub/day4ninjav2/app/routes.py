import flask

from app import app, db, forms, models
import requests
from wtforms import validators
from flask import redirect, render_template, request, flash, url_for
from app.models import Todolist


# db.create_all()


@app.route('/', methods=['GET', 'POST'])
def todo_list():
    todos = models.Todolist.query.all()
    return flask.render_template("todolist.html", todos=todos)

@app.route('/add', methods=['GET', 'POST'])
def add_list():
    form1 = forms.Todolist1()
    if flask.request.method == "POST":
        if form1.validate_on_submit():
            todo1 = forms.Todolist1().todo.data
            item = models.Todolist(todo=todo1)
            item.save()
            return redirect("/")
    return render_template('additem.html', form1=form1)

@app.route("/check/<int:id>")
def checktodo(id):

    # Retrieve the Todo object
    todo = models.Todolist.query.get(id)

    # Marking todo.done as True
    todo.check = True

    # Commit our changes to the database
    db.session.commit()

    # Redirecting to home page
    return flask.redirect("/")


# db.create_all()
# to1 = Todolist(todo = 'Walk the Dog', check = False)
# to2 = Todolist(todo = 'Take out the trash', check = False)
# to3 = Todolist(todo = 'Do the dishes', check = False)
# db.session.add(to1)
# db.session.add(to2)
# db.session.add(to3)
# db.session.commit()
# db.drop_all()
#
