# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex Teams bot in Python"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello PIW attendees"

app.run(port=2099)
