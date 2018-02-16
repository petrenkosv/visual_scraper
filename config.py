import os

basedir = os.path.abspath(os.path.dirname(__file__))

class Config(object):
    SECRET_KEY = os.environ.get('SECRET_KEY') or 'you-will-never-guess'
    POSTGRES = {
        'user':'greg',
        'pw':'lackey',
        'db':'visual_scraper',
        'host':'localhost',
        'port':'5432',
    }

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or \
            'postgresql://%(user)s:%(pw)s@%(host)s:%(port)s/%(db)s' % POSTGRES
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    ADMINS= ['gdl5014@gmail.com']
    UPLOAD_FOLDER = os.path.join(basedir,'scrape_docs')
