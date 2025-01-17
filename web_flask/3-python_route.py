#!/usr/bin/python3
"""Starts a Flask web application with multiple routes and default values."""

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Route that displays 'Hello HBNB!'."""
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Route that displays 'HBNB'."""
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """Route that displays 'C ', followed by the value of the text variable."""
    text = text.replace('_', ' ')
    return "C " + text


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_text(text):
    """Route that displays 'Python ', followed by the value of the
    text variable (with default 'is cool')."""
    text = text.replace('_', ' ')
    return "Python " + text


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
