#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", defaults={'id': None}, strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id):
    """Displays an HTML page with a list of states sorted by name"""
    states = storage.all(State)
    if id:
        id = 'State.' + id
    return render_template('9-states.html', states=states, id=id)


@app.teardown_appcontext
def close_db(exception):
    """Closes the database after a request has been processed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=False)
