#!/usr/bin/env python
# -*- coding: utf-8 -*-

from flask import Flask, Response, jsonify, request, g, Blueprint
from flask.ext.login import LoginManager, UserMixin, login_required
from itsdangerous import (
    JSONWebSignatureSerializer,
    TimedJSONWebSignatureSerializer,
    BadSignature,
    SignatureExpired
)
import error_handlers

app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)

app.register_blueprint(error_handlers.blueprint)

class User(UserMixin):
    # proxy for a database of users
    user_database = {"JohnDoe": ("JohnDoe", "John"),
                     "JaneDoe": ("JaneDoe", "Jane")}

    def __init__(self, username, password):
        self.username = username
        self.password = password

    @classmethod
    def get(cls, username):
        return cls.user_database.get(username)


def verify_auth_token(token):
    s = TimedJSONWebSignatureSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None    # valid token, but expired
    except BadSignature:
        return None    # invalid token

    if not data['secret']:
        user_entry = User.get(data['username'])
        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1])
            if (user.password == data['password']):
                g.user = user
            return user

    return None


def verify_auth_secret_token(token):
    s = JSONWebSignatureSerializer(app.config['SECRET_KEY'])
    try:
        data = s.loads(token)
    except SignatureExpired:
        return None    # valid token, but expired
    except BadSignature:
        return None    # invalid token

    if data['secret']:
        user_entry = User.get(data['username'])
        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1])
            if (user.password == data['password']):
                g.user = user
                return user

    return None


def generate_token():

    """ Access Token """
    access_token_serializer = TimedJSONWebSignatureSerializer(
                            app.config['SECRET_KEY'],
                            expires_in=app.config['EXPIRES_IN'])

    """ Secret Token """
    secret_token_serializer = JSONWebSignatureSerializer(
                            app.config['SECRET_KEY'])

    d = {'username': g.user.username, 'password': g.user.password}

    d_access = d.copy()
    d_access.update({'secret': False})

    d_secret = d.copy()
    d_secret.update({'secret': True})

    access_token = access_token_serializer.dumps(d_access)
    secret_token = secret_token_serializer.dumps(d_secret)

    return access_token, secret_token


@login_manager.request_loader
def load_user(request):

    username_or_token = request.form['username']
    password = request.form['password']

    if username_or_token and password:
        user = verify_auth_token(username_or_token)
        if not user:
            user_entry = User.get(username_or_token)
            if (user_entry is not None):
                user = User(user_entry[0], user_entry[1])
                if (user.password != password):
                    return None

        g.user = user
        return user

    return None


@app.route("/", methods=["GET"])
def index():
    return Response(response="Hello World!", status=200)


@app.route("/login", methods=["POST"])
@login_required
def protected():
    access_token, secret_token = generate_token()
    data = {
                'status': 200,
                'message': "success",
                'data': 'Hello, %s!' % g.user.username,
                'secret_token': secret_token,
                'access_token': access_token
            }
    return jsonify(data)


@app.route("/profile", methods=["GET"])
@login_required
def profile():
    data = {
                'status': 200,
                'data': 'Hello, %s!' % g.user.username
            }
    return jsonify(data)


@app.route("/token", methods=["GET"])
def token():
    username_or_token = request.form['username']
    user = verify_auth_secret_token(username_or_token)

    if user:
        access_token, secret_token = generate_token()
        data = {
                    'status': 200,
                    'message': "success",
                    'data': 'Hello, %s!' % g.user.username,
                    'secret_token': secret_token,
                    'access_token': access_token
                }
        return jsonify(data)
    else:
        return forbidden()


if __name__ == '__main__':
    app.config['SECRET_KEY'] = ("3erlari-lari ke Kalasan "
                            "[20&#^))@__#*)@)@] ketemu "
                            "bidadari pada bejejeraN"
                            )
    app.config['EXPIRES_IN'] = 100
    app.run(port=5000, debug=True)
