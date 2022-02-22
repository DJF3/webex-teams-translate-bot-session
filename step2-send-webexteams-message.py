# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex bot in Python"
from webexteamssdk import WebexTeamsAPI
import os

# put your bot token in an environment variable 'PIW_BOT_TOKEN' OR replace below with: 
# BOT_TOKEN = "put_bot_token_here"
BOT_TOKEN = os.environ.get('PIW_BOT_TOKEN')
api = WebexTeamsAPI(access_token=BOT_TOKEN)

api.messages.create(toPersonEmail="YOUR_EMAIL_ADDRESS", markdown="Cisco Partners are the best")

# Then run this code and check if you received a message from the bot.
