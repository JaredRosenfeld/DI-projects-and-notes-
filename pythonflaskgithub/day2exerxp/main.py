import flask
from flask import request
from flask import render_template_string, render_template
import database_manager
from datetime import datetime

database_manager.create_database()


# with open('product_db.json', 'r') as prod:
#     data = prod.read()
#     for k in data:
#         print(k)

app = flask.Flask(__name__)

list1 = []

@app.route("/homepage")
def homepage():
    hour = datetime.now()
    now_hour = hour.hour
    return render_template('homepage.html', now_hour = now_hour)

@app.route("/homepage/category")
def category():
    list1 = []
    data = database_manager.load_database()
    for products in data:
        for k, v in products.items():
            if k == 'Category':
              if v not in list1:
                  list1.append(v)
    template_file = open('templates/category.html', 'r').read()
    return flask.render_template_string(template_file, product = products,data = data,list1 = list1)

@app.route("/homepage/category/<tech>")
def category_search(tech = None):
    techs = []
    data = database_manager.load_database()
    for d in data:
        if d['Category'] == tech:
            techs.append(d)
    template_file = open('templates/categorytech.html', 'r').read()
    return flask.render_template_string(template_file,tech = techs)


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

@app.route("/homepage/<name>/<int:quantity>")
def quantity_search(name = None, quantity = None):
    data = database_manager.load_database()
    for d in data:
        pass
    template_file = open('templates/quantity.html','r').read()
    return  flask.render_template_string(template_file, d = d,data = data, name = name, quantity = quantity)



if __name__ == "__main__":
    app.run(debug=True,port=5000)