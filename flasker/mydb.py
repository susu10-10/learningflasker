from enum import unique
from flask_sqlalchemy import SQLAlchemy

from hello import name
from datetime import datetime


# initialize the database
db = SQLAlchemy(app)

# create Model

class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(50), nullable=False)
    email = db.Column(db.String(40), nullable=False, unique=True)
    date_added = db.Column(db.DateTime, default=datetime.utcnow)


    # Create a String
    def __repr__(self):
        return '<Name %r>' % self.name