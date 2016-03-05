# Basic Url-Shortener
#
#

import os
import string
import random

from flask import Flask
from flask import render_template
from flask import redirect
from flask import url_for
from flask.ext.sqlalchemy import SQLAlchemy

################################## CONFIG ######################################
app = Flask(__name__)
app.config.from_object(os.environ['APP_SETTINGS'])
db = SQLAlchemy(app)

from models import URL
from forms import URLShortenerForm

################################# LIBRARY ######################################
# Generate validation string
def id_generator(size=8, chars=string.ascii_uppercase + string.ascii_lowercase + string.digits):
    return ''.join(random.choice(chars) for _ in range(size))

################################## ROUTES ######################################
@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLShortenerForm()
    if form.validate_on_submit():
        url = form.url.data
        existing_url = URL.query.filter_by(url=url).first()
        if existing_url:
            return render_template('index.html', form=form,
                url_shortened=existing_url.url_shortened,
                site_address=os.environ['SITE_ADDRESS'])
        else:
            new_url = URL(url=url, url_shortened=id_generator())
            db.session.add(new_url)
            db.session.commit()
            return render_template('index.html', form=form,
                url_shortened=new_url.url_shortened,
                site_address=os.environ['SITE_ADDRESS'])
    return render_template('index.html', form=form)

@app.route('/<url>')
def url(url):
    existing_url = URL.query.filter_by(url_shortened=url).first()
    if existing_url:
        return redirect(existing_url.url)
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
