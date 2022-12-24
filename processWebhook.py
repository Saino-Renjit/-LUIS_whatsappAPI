import os
import requests
import json

import flask
from flask import send_from_directory, request

app = flask.Flask(__name__)

@app.route('/')
@app.route('/home')
def home():
    return "Hello World"

from helperfunction.waSendMessage import sendMessage

@app.route('/whatsapp', methods=['GET', 'POST'])
def whatsapp():
    
    query= "https://zxcvbnm.cognitiveservices.azure.com/luis/prediction/v3.0/apps/5a60d162-2a8b-4c82-984c-3b38870b3c5a/slots/production/predict?verbose=true&show-all-intents=true&log=true&subscription-key=4ca9b36a470e404f83a9c3d065794eb1&query="
    whatsapp_message = request.form['Body']
    message=query+whatsapp_message

    response_API = requests.get(message)

    data = response_API.text
    parse_json =json.loads(data)
    senderId = request.form['From'].split('+')[1]
    try:
        result=parse_json['prediction']['entities']['RestaurantReservation.Time']
        s1= str(result)
        
        s2='Your booking schedule is updated to :'
        output="".join([s2, s1])
    except:
        output='Please specify the time for which the reservation is required.'
    
    
    res = sendMessage(senderId=senderId, message=output)
    print(f'This is the entity --> {res}')
    
    return '200'

if __name__ == "__main__":
    app.run(port=5000, debug=True)