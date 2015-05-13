#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, Response
from sepat import sepat
from wader import wader
from cupang import cupang


app = Flask('blueprints_example')
app.register_blueprint(sepat, url_prefix='/sepat')
app.register_blueprint(wader, url_prefix='/wader')
app.register_blueprint(cupang, url_prefix='/cupang')


@app.route('/', methods=['GET'])
def index():
    return Response(response="Hello World!", status=200)


@app.route('/unauthorized', methods=['GET'])
def unauthorized_page():
    return Response(response="401: Unauthorized", status=401)


@app.errorhandler(403)
def forbidden(error=None):
    return Response(response="403: Forbidden mas!", status=403)


if __name__ == '__main__':
    app.run('0.0.0.0', debug=True)
