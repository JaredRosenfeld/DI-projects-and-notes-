import flask
from flask import request
from flask import render_template_string, render_template
import database_manager

database_manager.create_database()


# with open('product_db.json', 'r') as prod:
#     data = prod.read()
#     for k in data:
#         print(k)

app = flask.Flask(__name__)


@app.route("/homepage")
def homepage():
    return render_template('homepage.html')

@app.route("/homepage/products")
def products():
    data = database_manager.load_database()
    template_file = open('templates/products.html', 'r').read()
    return flask.render_template_string(template_file, data = data)

@app.route("/homepage/products/<product_id>")
def product_info(product_id):
    ids = {}
    data = database_manager.load_database()
    for d in data:
        if d['ProductId'] == product_id:
            ids = d
    template_file = open('templates/product_info.html', 'r').read()
    return flask.render_template_string(template_file, products = ids)


if __name__ == "__main__":
    app.run(debug=True,port=5000)