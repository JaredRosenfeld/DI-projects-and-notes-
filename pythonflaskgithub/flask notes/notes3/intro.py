import flask
from flask import Flask
from flask import render_template_string, render_template

app = flask.Flask(__name__)
print(__name__)

# @app.route('/home/<username>')
# def index(username):
#     template_string =  '''
#         <html>
#             <head>
#                 <title>Home Page - Microblog</title>
#             </head>
#             <body>
#                 <h1>Hello, {{ name }}! How are you ?</h1>
#             </body>
#         </html>
#     '''
#     html = flask.render_template_string(template_string, name=username)
#     return html
# @app.route('/')
# def index():
#     my_template = '''
#         <html>
#             <head>
#                 <title>Home Page - Microblog</title>
#             </head>
#             <body>
#                 <h1>{{ firstname }} {{ lastname }} says: Wubbalubbadubdub!</h1>
#             </body>
#         </html>
#     '''
#
#     html = render_template_string(my_template, firstname="Rick", lastname="Sanchez")
#     return html

# def blog_return():
#     list_of_users = ['Joe', 'Bob','Simon']
#     string = ''
#     for i in list_of_users:
#         string += i
#         string += ' '
#     return string

@app.route('/blog')
def blog_main():
    my_template = '''
    <html>
             <head>
                 <title>Home Page - First Blog Page</title>
             </head>
             <body>
                 <h1>Hi Users welcome to Jared's Blog</h1>
             </body>
         </html>
     '''
    return my_template

@app.route('/blog/<username>/articles')
def blog_articles(username):
    my_template = '''
        <html>
                 <head>
                     <title>Hi there {{username}} welcome to your page</title>
                 </head>
                 <body>
                     <h1>Hi there {{username}} welcome to your pag</h1>
                     <h2>Here are a list of the article subject: {{article1}}</h2>
                     <h3>{{article2}}</h3>
                     <h4>{{article3}}</h4>
                 </body>
             </html>
         '''
    html = render_template_string(my_template,article1 = 'Dogs', article2= 'Cats', article3 = 'fish')
    return html
@app.route('/index')
def index1():
    return render_template('index.html')

@app.route('/about ')
def index2():
    return render_template('about.html')

# @app.route('/<username>')
# def hello_world(username = None):
#     return render_template('index.html',name =

@app.route('/<username>/<int:post_id>')
def hello_world(username = None,post_id = None):
    return render_template('index.html',name = username, post_id = post_id)
if __name__ == "__main__":
    app.run(debug=True,port=5000)