from flask import Flask
app = Flask(__name__)
print(__name__)

@app.route('/')
def hello_world():
    return 'Hello, Jared Rosenfeld!'
# create virtualenv c:\>python -m venv c:\path\to\myenv
# go to activate.bat run it
# set flask_app = 'creatingserver.py'
# python3 - m flask run
# set FLASK_ENV = "development"
# if ununable to load run:
# python3 <name>.py
