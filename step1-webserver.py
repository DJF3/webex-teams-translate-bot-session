# -*- coding: utf-8 -*-
# by DJ Uittenbogaard - duittenb@cisco.com
# Code is part of a session for partners "create a Webex bot in Python"
from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return "Hello PIW attendees"

app.run(port=2099)

# run this python code and browse to 'http://localhost:2099'
