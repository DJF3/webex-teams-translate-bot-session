# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex Teams bot in Python"
from webexteamssdk import WebexTeamsAPI
import os

BOT_TOKEN = os.environ.get('PIW_BOT_TOKEN')
# OR --> BOT_TOKEN = "put_bot_token_here"
api = WebexTeamsAPI(access_token=BOT_TOKEN)

api.webhooks.create("Partner Bot Demo webhook 2020", "bot_webhook_url_here", "messages", "created")
