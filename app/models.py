from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime
from flask_login import UserMixin
from hashlib import md5
from app import app, db, login
from time import time
import jwt


class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), index= True, unique = True)
    email = db.Column(db.String(120), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def avatar(self,size):
        digest = md5(self.email.lower().encode('utf-8')).hexdigest()
        return 'https://www.gravatar.com/avatar/{}?d=identicon&s={}'.format(
            digest, size)
    last_seen = db.Column(db.DateTime,default=datetime.utcnow)

class Test(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    doc_path = db.Column(db.String(500), index=True,unique=True)
    doc_name = db.Column(db.String(100), index=True,unique=True)
    api_number = db.Column(db.String(12), index=True)
    test_date = db.Column(db.Date)
    initial_pressure = db.Column(db.REAL)
    final_pressure = db.Column(db.REAL)
    buildup_pressure = db.Column(db.REAL)
    water_flow = db.Column(db.Boolean, default='False')
    oil_flow = db.Column(db.Boolean, default='False')
    scraped = db.Column(db.Boolean, default='False')
    scraper_name = db.Column(db.String(64))

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

