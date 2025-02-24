#!/usr/bin/python3
"""
Starts a Flask web application with routes.
"""
from flask import Flask, render_template

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
    return 'C ' + text.replace("_", " ")


@app.route('/python/')
@app.route('/python/<text>')
def python_text(text='is cool'):
    """Display 'Python ' followed by the value of the text variable"""
    return 'Python ' + text.replace("_", " ")


@app.route('/number/<int:n>')
def number(n):
    """Display 'n is a number' only if n is an integer"""
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>')
def number_template(n):
    """Display a HTML page only if n is an integer"""
    return render_template('6-number_odd_or_even.html', n=n)


@app.route('/number_odd_or_even/<int:n>')
def number_odd_or_even(n):
    """Display a HTML page only if n is an integer"""
    odd_or_even = 'even' if n % 2 == 0 else 'odd'
    return render_template(
        '6-number_odd_or_even.html',
        n=n,
        odd_or_even=odd_or_even
    )


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
