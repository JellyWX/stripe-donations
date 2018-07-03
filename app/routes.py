from flask import redirect, url_for, render_template, request, session, abort, jsonify
from app import app, discord, db
from app.models import SimpleUser
import stripe


@app.route('/')
@app.route('/index')
def index():
    if not discord.authorized: # force oauth to access page
        return redirect(url_for('discord.login'))


    discord_user = discord.get('api/users/@me').json() # grab user

    if SimpleUser.query.filter_by(email=discord_user['email']).first() is None: # check if the user is registered already

        user = SimpleUser(user_id=discord_user['id'], email=discord_user['email'], username=discord_user['username'])

        db.session.add(user)
        db.session.commit() # commit to the DB

    return render_template('index.html', key=app.config['STRIPE_PUBLIC'])


@app.route('/charge', methods=['POST'])
def charge():
    if not discord.authorized: # force oauth to access page
        return redirect(url_for('discord.login'))

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

@app.route('/api/user/email/<int:id>', methods=['GET'])
def user_subscriptions(id):
    user = SimpleUser.query.filter_by(user_id=id).first()

    if user is None:
        abort(404)

    else:
        return jsonify({'id': user.user_id, 'email': user.email})
