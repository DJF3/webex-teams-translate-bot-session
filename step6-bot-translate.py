# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex Bot in Python"
from flask import Flask, jsonify, request
from webexteamssdk import WebexTeamsAPI
import os
import json
import requests

# put your bot token in an environment variable 'PIW_BOT_TOKEN' OR replace below with: BOT_TOKEN = "put_bot_token_here"
TRANSLATE_TOKEN = os.environ.get('PIW_TRANSLATE_TOKEN')
BOT_TOKEN = os.environ.get('PIW_BOT_TOKEN')
SUPPORTED_LANGUAGES = ('nl', 'de', 'en', 'fr', 'es')  # add more language codes if needed

api = WebexTeamsAPI(access_token=BOT_TOKEN)
app = Flask(__name__)


# function to translate 'text' into destination language 'lang'
def translate(lang, text):
    url = "https://kiara-translate-v2.p.rapidapi.com/v2/translate"
    payload = '{ "inputText": "' + text + '", "targetLanguage": "' + lang + '"}'
    headers = {'x-rapidapi-host': "kiara-translate-v2.p.rapidapi.com", 'x-rapidapi-key': TRANSLATE_TOKEN, \
    'content-type': "application/json", 'accept': "application/json"}
    response = requests.request("POST", url, data=payload.encode('utf-8'), headers=headers)
    print(response.text)
    return(response.text)


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
        # ___ capture first 2 characters from msg text (language)
        #     my_message:  "de buy an applepie"
        my_language = my_message.split()[0].lower().strip()
        #     my_language:  "de"
        # ___ capture text to be translated
        my_text = " ".join(my_message.split()[1:])
        #     example:  "buy an applepie"

        # ___ check if language to make sure it's a valid language
        if my_language in SUPPORTED_LANGUAGES:
            # translate my_text to the destination language my_language
            my_translation = translate(my_language, my_text)
            # json data with translation returned - extract 'translatedText'
            my_translation = json.loads(my_translation)['translatedText']
            print(f">> TRANSLATION: {my_translation}")
            # send translated message back to the user
            api.messages.create(toPersonId=message.personId, markdown=my_translation)
        else:
            # NOT OK? --> send help text
            return_text = "please start your message with the language code: " + " ".join(SUPPORTED_LANGUAGES) + " followed by the text to translate"
            api.messages.create(toPersonId=message.personId, markdown=return_text)

    return jsonify({"success": True})


app.run(host='0.0.0.0', port=2099, debug=True)

# Run this code and send "nl applepie" to the bot. It should return 'applepie' translated to 'nl' (Dutch) = "appeltaart"
