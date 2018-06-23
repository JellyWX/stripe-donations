from flask import redirect, url_for, render_template, request, session
from app import app, discord, db
from models import SimpleUser
import stripe


@app.before_request
def before_request():
    if not discord.authorized: # force oauth to access page
        return redirect(url_for('discord.login'))


@app.route('/')
@app.route('/index')
def index():
    discord_user = discord.get('api/users/@me').json() # grab user

    if SimpleUser.query.filter_by(email=discord_user['email']) is None: # check if the user is registered already

        user = SimpleUser(user_id=discord_user['id'], email=discord_user['email'], username=discord_user['username'])

        db.session.add(user)
        db.session.commit() # commit to the DB

    return render_template('index.html', key=config['STRIPE_PUBLIC'])


@app.route('/charge')
def charge():
    user = discord.get('api/users/@me').json()

    customer = stripe.Customer.create(
        email=user['email'],
        source=request.form['stripeToken']
    )

    charge = stripe.Subscription.create(
        customer=customer.id,
        items=[
            {'plan': 'plan_D3QO1EpbGsFVMK'}
        ]
    )

    return render_template('charge.html')
