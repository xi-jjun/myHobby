# /usr/bin/env python
# Download the twilio-python library from twilio.com/docs/libraries/python
import os
from twilio.rest import Client

# Find these values at https://twilio.com/user/account
# To set up environmental variables, see http://twil.io/secure
account_sid = 'ACb11b65bc44d629b3a688e7c8f3b534cc'
auth_token = 'ba17ebde598ea3eaeed0326aa8054814'

client = Client(account_sid, auth_token)

client.api.account.messages.create(
    to="+821023090329",                  # my phone
    from_="+13237460677",   # twilio
    body="안녕? 코딩으로 보낸 메세지야 도연아")    # message