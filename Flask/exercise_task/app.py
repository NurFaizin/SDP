#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask
from flask.ext.login import LoginManager

# Create Flask app
app = Flask(__name__)

# Token for app
app.config['SECRET_KEY'] = ("3erlari-lari ke Kalasan "
                        "[20&#^))@__#*)@)@] ketemu "
                        "bidadari pada bejejeraN"
                        )
app.config['EXPIRES_IN'] = 1000

# Associate Flask-Login manager with current app
login_manager = LoginManager()
login_manager.init_app(app)