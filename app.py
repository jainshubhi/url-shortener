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

# take only important part of url
def remove_slashes(url):
    return url.split('//')[1]

################################## ROUTES ######################################
@app.route('/', methods=['GET', 'POST'])
def index():
    form = URLShortenerForm()
    if form.validate_on_submit():
        url = remove_slashes(form.url.data)
        existing_url = URL.query.filter_by(url=url).first()
        if existing_url:
            # url is already in db so serve that shortened url
            return render_template('index.html', form=form,
                url_shortened=existing_url.url_shortened,
                site_address=os.environ['SITE_ADDRESS'])
        else:
            # make sure shortened_url doesn't already exist
            le_id = id_generator()
            while URL.query.filter_by(url_shortened=le_id).first():
                le_id = id_generator()
            # add url to db
            new_url = URL(url=url, url_shortened=le_id)
            db.session.add(new_url)
            db.session.commit()
            return render_template('index.html', form=form,
                url_shortened=new_url.url_shortened,
                site_address=os.environ['SITE_ADDRESS'])
    return render_template('index.html', form=form)

@app.route('/<url>')
def url(url):
    existing_url = URL.query.filter_by(url_shortened=url).first()
    # if shortened url exists
    if existing_url:
        return redirect('https://' + existing_url.url)
    # redirect to mainpage if this is a random url
    else:
        return redirect(url_for('index'))


if __name__ == '__main__':
    app.run()
