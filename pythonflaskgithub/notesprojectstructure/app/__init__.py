from flask import Flask

app = Flask(__name__) # Remember: __name__ is the name of the file where the code is written

from app import routes, error_handlers
from errorhandler import ErrorHandler