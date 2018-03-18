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
    docs = db.relationship('Documents', backref='scraper',lazy='dynamic')

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


class Documents(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    doc_path = db.Column(db.String(500), index=True,unique=True)
    doc_name = db.Column(db.String(100), index=True,unique=True)
    api_number = db.Column(db.String(12), index=True)
    test_date = db.Column(db.Date)
    init_bradenhead_pressure = db.Column(db.REAL)
    init_intermediate_1_pressure = db.Column(db.REAL)
    init_intermediate_2_pressure = db.Column(db.REAL)
    init_casing_pressure = db.Column(db.REAL)
    init_tubing_pressure = db.Column(db.REAL)
    fin_bradenhead_pressure = db.Column(db.REAL)
    fin_intermediate_1_pressure = db.Column(db.REAL)
    fin_intermediate_2_pressure = db.Column(db.REAL)
    fin_casing_pressure = db.Column(db.REAL)
    fin_tubing_pressure = db.Column(db.REAL)
    bradenhead_buildup_pressure = db.Column(db.REAL)
    intermediate_1_buildup_pressure = db.Column(db.REAL)
    intermediate_2_buildup_pressure = db.Column(db.REAL)
    comment = db.Column(db.String(1000))
    shut_in = db.Column(db.Boolean, default='False') 
    water_flow = db.Column(db.Boolean, default='False')
    oil_flow = db.Column(db.Boolean, default='False')
    scraped = db.Column(db.Boolean, default='False')
    scraper_name = db.Column(db.String(64))
    scraper_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    date_scraped = db.Column(db.Date)
    user_id = db.Column(db.Integer)
    in_use = db.Column(db.Boolean, default='False')

    def __repr__(self):
        return '<Document {}>'.format(self.doc_name)

class PrevDoc(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    doc_id = db.Column(db.Integer)
    doc_path = db.Column(db.String(500), index=True,unique=True)
    doc_name = db.Column(db.String(100), index=True,unique=True)
    api_number = db.Column(db.String(12), index=True)
    test_date = db.Column(db.Date)
    init_bradenhead_pressure = db.Column(db.REAL)
    init_intermediate_1_pressure = db.Column(db.REAL)
    init_intermediate_2_pressure = db.Column(db.REAL)
    init_casing_pressure = db.Column(db.REAL)
    init_tubing_pressure = db.Column(db.REAL)
    fin_bradenhead_pressure = db.Column(db.REAL)
    fin_intermediate_1_pressure = db.Column(db.REAL)
    fin_intermediate_2_pressure = db.Column(db.REAL)
    fin_casing_pressure = db.Column(db.REAL)
    fin_tubing_pressure = db.Column(db.REAL)
    bradenhead_buildup_pressure = db.Column(db.REAL)
    intermediate_1_buildup_pressure = db.Column(db.REAL)
    intermediate_2_buildup_pressure = db.Column(db.REAL)
    comment = db.Column(db.String(1000))
    shut_in = db.Column(db.Boolean, default='False')
    water_flow = db.Column(db.Boolean, default='False')
    oil_flow = db.Column(db.Boolean, default='False')
    scraped = db.Column(db.Boolean, default='False')
    scraper_id = db.Column(db.Integer, db.ForeignKey('user.id'))
    scraper_name = db.Column(db.String(64))
    date_scraped = db.Column(db.Date)
    user_id = db.Column(db.Integer)
    in_use = db.Column(db.Boolean, default='False')

    def __repr__(self):
        return '<Document {}>'.format(self.doc_name)

@login.user_loader
def load_user(id):
    return User.query.get(int(id))

