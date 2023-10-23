#!/usr/bin/python3
"""Starts a Flask web application to display a list of cities by states."""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name)


@app.route('/cities_by_states', strict_slashes=False)
def cities_by_states():
    """Display a list of states and their associated cities."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('8-cities_by_states.html', states=sorted_states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
