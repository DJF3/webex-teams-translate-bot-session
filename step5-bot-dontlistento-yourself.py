# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex bot in Python"
from flask import Flask, jsonify, request
from webexteamssdk import WebexTeamsAPI
import os

# put your bot token in an environment variable 'PIW_BOT_TOKEN' OR replace below with: BOT_TOKEN = "put_bot_token_here"
BOT_TOKEN = os.environ.get('PIW_BOT_TOKEN')
api = WebexTeamsAPI(access_token=BOT_TOKEN)
app = Flask(__name__)


@app.route('/', methods=["POST"])
def webhook():
    # get the webhook json message:
    json_payload = request.json
    # use message ID to read the message
    message = api.messages.get(json_payload['data']['id'])
    # extract message text from the message
    my_message = message.text
    # do not respond to messages from the bot itself
    if "@webex.bot" in message.personEmail:
        print("** NOT RESPONDING TO OWN MESSAGE!! **")
        pass
    else:
        print(f"the message TEXT is: {my_message}")
        api.messages.create(toPersonId=message.personId, markdown="welcome to this session")

    return jsonify({"success": True})

app.run(host='0.0.0.0', port=2099, debug=True)

# Run this code and send a message to the bot. It will respond with "welcome to this session"
