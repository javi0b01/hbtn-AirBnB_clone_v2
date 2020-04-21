#!/usr/bin/python3
""" Task 0. Hello Flask! """
from flask import Flask
my_app = Flask(__name__)


@my_app.route('/', strict_slashes=False)
""" decorator """


def my_hello():
    """ function """
    return 'Hello, HBNB!'

if __name__ == "__main__":
    """ conditional """
    my_app.run(host="0.0.0.0", port=5000)
