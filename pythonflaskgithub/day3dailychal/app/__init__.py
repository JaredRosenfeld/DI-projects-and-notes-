import flask
import static as static

app = flask.Flask(__name__) # Remember: __name__ is the name of the file where the code is written
# app._static_folder = app/static
from app import routes