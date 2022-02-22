# webex-bot-session
Code used in session for Cisco Partners. Topic: Webex bots in Python.


# Requirements
- Webex Message account [free](https://www.webex.com/team-collaboration.html) 
- Python 3.x [download](https://www.python.org/downloads/)
- Ngrok [download](https://ngrok.com/download)
- Libraries (webexteamssdk, requests, flask) (see below)
- Kiara translate account via RapidAPI [link](https://rapidapi.com/kiara-inc-kiara-inc-default/api/kiara-translate-v2/pricing)


# Install libraries

> pip install webexteamssdk

> pip install flask

> pip install requests



# GOAL

Create a Webex Bot that translates text from a detected language to a configured destination language.
Format:
> \<countrycode\> \<text_to_translate\>

Example:
> "de remember when we had live events with real people"

Will translate this scentence to 'de' (German)


# Steps

## Meet requirements

As listed above


## 1. Tiny webserver

Using flask: 

step1-webserver.py


## 2. Send Webex Teams Message

Using the Webex SDK - send message to Webex user:

step2-send-webexteams-message.py


## 3. Create Webhook

Using the Webex SDK - create a webhook for the bot:

step3-create-webhook.py


## 4. Bot: get message text

Get the actual message text: 

step4-bot-get-message.py


## 5. Bot: do not respond to own messages

Make the bot NOT respond to it's own messages

step5-bot-dontlistento-yourself.py


## 6. Bot: add translation component

Now add the final step that turns it into a translation bot!

step6-bot-translate.py


# More info

- Translation service: [Kiara Translation API v2](https://rapidapi.com/kiara-inc-kiara-inc-default/api/kiara-translate-v2/pricing)
- Code used in this session: https://github.com/DJF3/webex-teams-bot-session

**Webex Developer News**
http://cs.co/webexdevlink 

**The ultimate Webex Developer Resources**
http://cs.co/webexdevinfo



