import flask
from flask import url_for
from werkzeug.utils import redirect

from app import app

@app.errorhandler(404)
def error_404(error):
    return flask.render_template('errors/404_error.html'), 404

@app.errorhandler(500)
def error_500(error):
    return flask.render_template('505_error.html'),500

