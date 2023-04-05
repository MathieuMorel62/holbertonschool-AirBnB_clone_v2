#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models import *

app = Flask(__name__)


@app.route("/hbnb_filters", strict_slashes=False)
def states_list():
    """Displays an HTML page with filters for states and amenities"""
    states = storage.all(State).values()
    amenities = storage.all(Amenity).values()
    return render_template(
        '10-hbnb_filters.html', states=states, amenities=amenities)


@app.teardown_appcontext
def close_db(exception):
    """Closes the database after a request has been processed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
