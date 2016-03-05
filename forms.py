from flask.ext.wtf import Form
from wtforms import StringField
from wtforms.validators import DataRequired
from wtforms.validators import URL

class URLShortenerForm(Form):
    url = StringField('url', validators=[DataRequired(), URL()])
