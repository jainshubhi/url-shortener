from app import db


class URL(db.Model):
    __tablename__ = 'urls'

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(), unique=True)
    url_shortened = db.Column(db.String())

    def __repr__(self):
        return '<id {}, url {}, url_shortened {}>'.format(id, url, url_shortened)
