# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex Teams bot in Python"
from webexteamssdk import WebexTeamsAPI
import os

# below: or BOT_TOKEN = "put_bot_token_here"
BOT_TOKEN = os.environ.get('PIW_BOT_TOKEN')
api = WebexTeamsAPI(access_token=BOT_TOKEN)

api.messages.create(toPersonEmail="YOUR_EMAIL_ADDRESS", markdown="Cisco Partners are the best")