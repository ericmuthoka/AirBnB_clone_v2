#!/usr/bin/python3
"""Starts a Flask web application to display a list of states."""

from flask import Flask, render_template
from models import storage
from models.state import State
app = Flask(__name)


@app.route('/states_list', strict_slashes=False)
def states_list():
    """Display a list of states from DBStorage."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('7-states_list.html', states=sorted_states)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
