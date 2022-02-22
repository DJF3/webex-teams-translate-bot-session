# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex bot in Python"
from webexteamssdk import WebexTeamsAPI
import os

# put your bot token in an environment variable 'PIW_BOT_TOKEN' 
BOT_TOKEN = os.environ.get('PIW_BOT_TOKEN')
# OR --> BOT_TOKEN = "put_bot_token_here"
api = WebexTeamsAPI(access_token=BOT_TOKEN)

api.webhooks.create("Partner Bot Demo webhook", "BOT_WEBHOOK_URL", "messages", "created")

# Run this script to create the Bot Webhook that notifies the "BOT_WEBHOOK_URL" when a new "message" is "created"
