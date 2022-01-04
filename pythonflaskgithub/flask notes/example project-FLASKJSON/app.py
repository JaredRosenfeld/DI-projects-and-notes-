import flask
import database_manager # this is our module

app = flask.Flask(__name__)
database_manager.create_database()

# @app.route("/")
# @app.route("/products")
# def products_page():
#     data = database_manager.load_database()
#     return """
#         Currently, we don't have any product to sell, sorry!
#     """

@app.route("/")
@app.route("/products")
def products_page():

    data = database_manager.load_database()
    template_file = open('my_template.jinja', 'r').read()
    additional_css   = open('style.css','r').read()
    return flask.render_template_string(template_file, products=data, additional_css=additional_css)


app.run(debug=True)



if __name__ == "__main__":
    app.run(debug=True,port=5000)