import flask
from flask import Flask
from flask import render_template_string, render_template
app = Flask(__name__)

@app.route("/main")
def main_page():
    return render_template('main1_page.html')

if __name__ == "__main__":
    app.run(debug=True,port=5000)