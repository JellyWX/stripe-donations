from flask import Flask
from config import Config
from flask_dance.contrib.discord import make_discord_blueprint, discord
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

app = Flask(__name__)
app.config.from_object(Config)
discord_blueprint = make_discord_blueprint(scope=['identify', 'guilds', 'email'], redirect_url='dashboard')
app.register_blueprint(discord_blueprint, url_prefix='/login')
db = SQLAlchemy(app)
migrate = Migrate(app, db)

from app import routes, models
