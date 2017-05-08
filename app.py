from flask import Flask
from flask import render_template
from flask import request
import os
import stripe

SECRET_KEY = 'sk_test_2CJHIv4WfHYYWkOpGsyHGI1F'
PUBLISHABLE_KEY = 'pk_test_8zlZgHy67wX0VfHzCbwDXf9Q'

stripe_keys = {
    'secret_key': SECRET_KEY,
    'publishable_key': PUBLISHABLE_KEY
    }

stripe.api_key = stripe_keys['secret_key']

app = Flask(__name__)

@app.route('/')
def index():
    """
    """
    return render_template('index.html', key=stripe_keys['publishable_key'])

@app.route('/pay')
def pay():
    """
    """
    amount = 500 # cents
    customer = stripe.Customer.create(
        email='shwetabh.sharan@forgeahead.io',
        source=request.form['stripeToken'])

    charge = stripe.Charge.create(customer=customer.id,
                                  amount=amount, currency='usd',
                                  description='school subscription payment')

    return render_template('pay.html', amount=amount)

if __name__ == '__main__':
    app.run(debug=True)
