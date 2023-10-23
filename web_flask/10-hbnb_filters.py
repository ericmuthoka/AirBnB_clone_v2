#!/usr/bin/python3
"""Starts a Flask web application to display an HBNB filters page."""

from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City
from models.amenity import Amenity
from werkzeug.exceptions import NotFound

app = Flask(__name)
app.url_map.strict_slashes = False


@app.route('/hbnb_filters')
def hbnb_filters():
    """Display an HBNB filters page."""
    states = sorted(storage.all(State).values(), key=lambda s: s.name)
    cities = sorted(storage.all(City).values(), key=lambda c: c.name)
    amenities = sorted(storage.all(Amenity).values(), key=lambda a: a.name)
    return render_template('10-hbnb_filters.html', states=states, cities=cities, amenities=amenities)


@app.teardown_appcontext
def close_session(exception):
    """Remove the current SQLAlchemy session after each request."""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
