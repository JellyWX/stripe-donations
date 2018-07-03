from flask import Flask
from config import Config
from flask_dance.contrib.discord import make_discord_blueprint, discord
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
import stripe

app = Flask(__name__)
app.config.from_object(Config)
discord_blueprint = make_discord_blueprint(scope=['identify', 'email'], redirect_url='index')
app.register_blueprint(discord_blueprint, url_prefix='/login')
db = SQLAlchemy(app)
migrate = Migrate(app, db)
stripe.api_key = app.config['STRIPE_SECRET']

from app import routes, models
