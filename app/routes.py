from flask import redirect, url_for, render_template, request, session
from app import app, discord, db
from models import SimpleUser



@app.route('/')
def index():
    pass


@app.route('/charge')
def charge():
    if not discord.authorized: # force oauth to access page
        return redirect(url_for('discord.login'))

    discord_user = discord.get('api/users/@me').json() # grab user

    if SimpleUser.query.filter_by(email=discord_user['email']) is None: # check if the user is registered already

        user = SimpleUser(user_id=discord_user['id'], email=discord_user['email'], username=discord_user['username'])

        db.session.add(user)
        db.session.commit() # commit to the DB
