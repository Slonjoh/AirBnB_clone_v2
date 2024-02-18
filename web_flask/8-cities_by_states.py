#!/usr/bin/python3
"""Script that starts a Flask web application"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.teardown_appcontext
def teardown_db(exception):
    """Remove the current SQLAlchemy Session"""
    storage.close()


@app.route('/cities_by_states')
def cities_by_states():
    """Display a HTML page with a list of all State objects and their cities"""
    states = storage.all(State).values()
    sorted_states = sorted(states, key=lambda state: state.name)
    return render_template("8-cities_by_states.html", states=sorted_states)


@app.after_request
def add_headers(response):
    response.headers['Server'] = "apache/2.4.7"
    return (response)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
