import flask

app = flask.Flask(__name__)


@app.route('/<int:number>')
def fib(number):
    fib = [0, 1]
    if number > 2:
        for i in range(2, number):
            nextElement = fib[i - 1] + fib[i - 2]
            fib.append(nextElement)
    template_file = open('templates/fibseq.html', 'r').read()
    fib_sum = sum(fib)
    return flask.render_template_string(template_file, f = fib ,fib_sum = fib_sum, number = number)




if __name__ == "__main__":
    app.run(debug=True, port=5000)
