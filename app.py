# Basic Url-Shortener
#
#

import os

from flask import Flask
from flask.ext.sqlalchemy import SQLAlchemy

################################## CONFIG ######################################
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import URL
################################## ROUTES ######################################
@app.route('/')
def index():
    return 'Hi'

@app.route('/<url>')
def url(url):
    return 'hi'

if __name__ == '__main__':
    app.run()
