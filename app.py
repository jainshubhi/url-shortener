# Basic Url-Shortener
#
#

import os

from flask import Flask


app = Flask(__name__)
# app.config.from_object(os.environ['APP_SETTINGS'])


@app.route('/')
def index():
    return 'Hi'

if __name__ == '__main__':
    app.run()