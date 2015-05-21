#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask
import routes
import error_handlers

app = Flask(__name__)
app.register_blueprint(routes.tasks)
app.register_blueprint(error_handlers.blueprint)

app.run(port=5000, debug=True)