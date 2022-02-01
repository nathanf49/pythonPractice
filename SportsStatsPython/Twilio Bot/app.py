# handles data for twilio bot

import os  # used to access environmental variables
from flask import Flask, request  # used to manage app
import requests # used to get data I think. May not be needed if I'm just returning data from nbaParser.py
from dateutil import parser, tz  # used to get time zone
from twilio.twiml.messaging_response import MessagingResponse  # for response message sent

app = Flask(__name__) # creates flask object

timezone = tz.gettz('America/New_York')


@app.route('/', methods=['POST']) # tells twilio to send a POST request to webhook below with contents of sms received

def receiveSMS():
    body = request.values.get('Body', None)  # gets body of request/text or None if it's blank
    response = MessagingResponse()  # makes MessagingResponse object (so methods will be available)
    response.message(body or 'Hello World!')  # replies with message sent or Hello World! if message was blank

if __name__ == '__main__':
    port = int(os.environ.get("PORT",5000))  # Runs on port 5000 by default or whatever PORT is defined as in .env
