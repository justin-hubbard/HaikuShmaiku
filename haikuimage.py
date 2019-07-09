#import twilio client

import requests
from flask import Flask
from flask import request, redirect
from flask import send_from_directory

from twilio.twiml.messaging_response import MessagingResponse
from twilio.rest import Client
from twilio import twiml

import picturemaker

# Srnd back account setup
account_sid = "AC4a0aa91206a688c09addf7655cc0b416"
auth_tok = "51fabc6f23213449481087c549ac0cdb"

#client = Client( account_sid, auth_tok)
#########################


UPLOAD_FOLDER = '/home/pi/Documents/PythonProjects/HaikuImage/uploads/'

app = Flask(__name__)
#app.config

#def send_image(recipient_num):

@app.route('/sms', methods=['POST', 'GET'])
def sms():
    #print("sms started")
    response = MessagingResponse()

    body = request.form['Body']

    if request.form['Body'] != '/0':
        print("Body of the text: ", body)
    else:
        print("It didn't work!!")

    #response.message("Successful text! (Message: {}".format(body))


    filename = request.form['MessageSid'] + '.png'
    picturemaker.generate_image(body, filename)
    with response.message() as message:
        message.body = "{0}".format("Here's your haiku")
        message.media('http://80b7dcaf.ngrok.io/uploads/{}'.format(filename))
    
    return str(response)

@app.route('/uploads/<filename>', methods=['GET','POST'])
def uploaded_files(filename):
    return send_from_directory(UPLOAD_FOLDER, filename)


if __name__ == "__main__":
    app.run(debug=True)
