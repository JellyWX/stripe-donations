import os
import configparser

class Config(object):
    basedir = './'

    config = configparser.SafeConfigParser()
    config.read(basedir + 'config.ini')
    client_id = config.get('WEB', 'DISCORD_OAUTH_CLIENT_ID')
    client_secret = config.get('WEB', 'DISCORD_OAUTH_CLIENT_SECRET')
    secret = config.get('WEB', 'SECRET')
    stripe_secret = config.get('WEB', 'STRIPE_SECRET')
    stripe_public = config.get('WEB', 'STRIPE_SECRET')

    SECRET_KEY = os.environ.get('SECRET_KEY') or secret

    DISCORD_OAUTH_CLIENT_ID = os.environ.get('DISCORD_OAUTH_CLIENT_ID') or client_id
    DISCORD_OAUTH_CLIENT_SECRET = os.environ.get('DISCORD_OAUTH_CLIENT_SECRET') or client_secret

    SQLALCHEMY_DATABASE_URI = os.environ.get('DATABASE_URL') or 'sqlite:///' + os.path.join(basedir, 'app.db')
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    STRIPE_SECRET = stripe_secret
    STRIPE_PUBLIC = stripe_public
