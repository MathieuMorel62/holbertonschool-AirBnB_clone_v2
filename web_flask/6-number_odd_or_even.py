#!/usr/bin/python3
"""Script that starts a Flask web application"""
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_hbnb():
    """ Route for the URL / """
    return "Hello HBNB!"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """ Route for the URL /hbnb """
    return "HBNB"


@app.route("/c/<text>", strict_slashes=False)
def c_txt(text):
    """ Dynamic route for the URL /c/<text> """
    return "C {}".format(text.replace('_', ' '))


@app.route("/python/", defaults={'text': 'is cool'}, strict_slashes=False)
@app.route("/python/<text>", strict_slashes=False)
def python_txt(text):
    """ Routes for the URL /python/ and /python/<text> """
    return "Python {}".format(text.replace('_', ' '))


@app.route("/number/<int:n>", strict_slashes=False)
def n_is_number(n):
    """ Route for the URL /number/<n>, only displays if n is an integer """
    return "{} is a number".format(n)


@app.route("/number_template/<int:n>", strict_slashes=False)
def n_template(n):
    """Route for the URL /number_template/<n> only displays if n is an int"""
    return render_template('5-number.html', number=n)


@app.route("/number_odd_or_even/<int:n>", strict_slashes=False)
def n_odd_or_even(n):
    """Route for the URL /number_odd_or_even/<n> only display if n is an int"""
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template(
        '6-number_odd_or_even.html', number=n, parity=odd_or_even)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
