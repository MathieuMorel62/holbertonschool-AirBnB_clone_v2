#!/usr/bin/python3
"""
Script that starts a Flask web application
"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.city import City

app = Flask(__name__)


@app.route("/states", strict_slashes=False)
@app.route("/states/<id>", strict_slashes=False)
def states_list(id=None):
    """Displays an HTML page with a list of all State objects or cities"""
    if id is None:
        states = storage.all(State).values()
        states_sorted = sorted(states, key=lambda state: state.name)
        return render_template('9-states.html', states=states_sorted)
    else:
        states = storage.all(State)
        state = states.get('State.{}'.format(id))
        if state:
            cities_sorted = sorted(state.cities, key=lambda city: city.name)
            return render_template(
                '9-states.html', state=state, cities=cities_sorted)
    return render_template('9-states.html', not_found=True)


@app.teardown_appcontext
def close_db(exception):
    """Closes the database after a request has been processed"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
