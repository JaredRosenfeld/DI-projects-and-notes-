from app import models, db

class Todo():
    def __init__(self,todo, is_todo_complete = False ):
        todo_text = todo
        todo_complete = is_todo_complete


    def get_todos(self):
        list_of_todos = models.Todolist.query.all()
        return list_of_todos
    def save_to_db(self,todo_text,todo_complete):
        db.session.add(todo_text,todo_complete)
        db.session.commit()
