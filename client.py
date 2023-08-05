import os
from twilio.rest import Client


# Find your Account SID and Auth Token at twilio.com/console
# and set the environment variables. See http://twil.io/secure
account_sid = os.environ['TWILIO_ACCOUNT_SID']
auth_token = os.environ['TWILIO_AUTH_TOKEN']
client = Client(account_sid, auth_token)

call = client.calls.create(
                        url='https://cce2-2601-647-6680-1580-78ac-2214-f878-3b1e.ngrok.io/twiml',
                        to='+14439179272',
                        from_='+16503003066'
                    )

print(call.sid)