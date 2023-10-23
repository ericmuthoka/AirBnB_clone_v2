#!/usr/bin/python3
"""Starts a Flask web application to display a list of states and cities."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from uuid import UUID
from flask import abort
from flask import jsonify
from werkzeug.exceptions import NotFound

app = Flask(__name)


@app.route('/states', strict_slashes=False)
def list_states():
    """Display a list of states and cities."""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda s: s.name)
    return render_template('9-states.html', states=sorted_states)


@app.route('/states/<id>', strict_slashes=False)
def state_cities(id):
    """Display a state and its cities."""
    try:
        state = storage.get(State, id)
        return render_template('9-states.html', states=[state])
    except Exception:
        return NotFound()


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
