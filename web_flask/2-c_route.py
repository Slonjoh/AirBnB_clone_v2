#!/usr/bin/python3
"""
Starts a Flask web application with routes.
"""
from flask import Flask
from urllib.parse import unquote

app = Flask(__name__)
app.url_map.strict_slashes = False


@app.route('/')
def hello_hbnb():
    """Display 'Hello HBNB!'"""
    return 'Hello HBNB!'


@app.route('/hbnb')
def hbnb():
    """Display 'HBNB'"""
    return 'HBNB'


@app.route('/c/<text>')
def c_text(text):
    """Display 'C ' followed by the value of the text variable"""
    return 'C ' + unquote(text).replace("_", " ")


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
