import os

from twilio.rest import Client

#from dotenv import load_dotenv
#load_dotenv()

ACCOUNT_SID='ACb68c762e025a1c97b1afd67a5f85f3cb'
AUTH_TOKEN='024f5f50477a7a45243463c098f727fd'
FROM='whatsapp:+14155238886'

client = Client(ACCOUNT_SID, AUTH_TOKEN)

def sendMessage(senderId, message):

    res = client.messages.create(
        body=message,
        from_=FROM,
        to=f'whatsapp:+{senderId}'
    )
    return res
