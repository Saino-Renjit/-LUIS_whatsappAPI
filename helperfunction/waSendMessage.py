import os

from twilio.rest import Client

#from dotenv import load_dotenv
#load_dotenv()

#ACCOUNT_SID = os.environ.get('ACCOUNT_SID')
#AUTH_TOKEN = os.environ.get('AUTH_TOKEN')
#FROM = os.environ.get('FROM')

ACCOUNT_SID='ACb68c762e025a1c97b1afd67a5f85f3cb'
AUTH_TOKEN='e1a482366aab8fb216d5f8bcd91da494'
FROM='whatsapp:+14155238886'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(senderId, message):

    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}'
    )
    return res
