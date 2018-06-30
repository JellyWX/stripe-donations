from app import db

class SimpleUser(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String)
    email = db.Column(db.String, index=True, unique=True)
    user_id = db.Column(db.Integer, unique=True)
    subscriptions = db.Column(db.String)
