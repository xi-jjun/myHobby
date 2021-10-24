# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = ''
auth_token = ''

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+82",                  # my phone
    from_="+1",   # twilio
    body="안녕? ")    # message
