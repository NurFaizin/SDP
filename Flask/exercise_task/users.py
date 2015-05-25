#!/usr/bin/env python
# -*- coding: utf-8 -*-


from app import app, login_manager
from database import connect, catch_error
from flask import g
from flask.ext.login import UserMixin
from itsdangerous import (
    JSONWebSignatureSerializer,
    TimedJSONWebSignatureSerializer,
    BadSignature,
    SignatureExpired
)


class User(UserMixin):
    """docstring for User"""


    def __init__(self, id, username, password, email):
        self.id = id
        self.username = username
        self.password = password
        self.email = email

    
    @classmethod
    def get(cls, username):

        # Open connection and execute SQL to create new user
        try:
            db, cursor = connect()

            cursor.execute("""SELECT id, username, password, email
                            FROM users
                            WHERE username='%s'""" % username)

            user_data = cursor.fetchone()

        # Get error messages
        except catch_error(), e:
            print "Error %d: %s" % (e.args[0],e.args[1])


        # Close connection
        finally:
            if db:
                db.close()

        if user_data:
            return (user_data['id'], user_data['username'], 
                    user_data['password'], user_data['email'])

        return None


@login_manager.request_loader
def load_user(request):

    access_token = request.args.get('access_token') \
                    or request.form.get('access_token')
    username = request.form.get('username')
    password = request.form.get('password')

    user = verify_auth_token(access_token)

    if not user:
        user_entry = User.get(username)

        if (user_entry is not None):
            user = User(user_entry[0], user_entry[1], 
                    user_entry[2], user_entry[3])

            if user.password != password:
                return None
    
    g.user = user
    return user


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

    # Open connection and execute SQL to create new user
    try:
        db, cursor = connect()

        cursor.execute("""INSERT INTO tokens (user_id, access_token, secret_token)
                        VALUES ('%s', '%s', '%s')""" % 
                        (g.user.id, access_token, secret_token)
                    )
        db.commit()

    # Get error messages
    except catch_error(), e:
        print "Error %d: %s" % (e.args[0],e.args[1])


    # Close connection
    finally:
        if db:
            db.close()

    return access_token, secret_token


def verify_auth_token(token):
    """Verify auth/access token"""

    # Open connection and execute SQL to create new user
    try:
        db, cursor = connect()

        cursor.execute("""SELECT access_token
                        FROM tokens
                        WHERE access_token='%s'""" % token)
        access_token = cursor.fetchone()

    # Get error messages
    except catch_error(), e:
        print "Error %d: %s" % (e.args[0],e.args[1])


    # Close connection
    finally:
        if db:
            db.close()

    # If access token match with token
    if access_token:
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
                user = User(user_entry[0], user_entry[1], 
                        user_entry[2], user_entry[3])

                if (user.password == data['password']):
                    g.user = user
                    return user

    return None


def verify_auth_secret_token(token):
    """Verify auth secret token"""

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
            user = User(user_entry[0], user_entry[1], 
                    user_entry[2], user_entry[3])

            if (user.password == data['password']):
                g.user = user
                return user

    return None


def create_user(user_data):
    """Create new user (register)"""

    username = user_data["username"]
    password = user_data["password"]
    email = user_data["email"]

    # Open connection and execute SQL to create new user
    try:
        db, cursor = connect()
        
        cursor.execute("""INSERT INTO users
                        (username, password, email)
                        VALUES (%s, %s, %s)
                        """,
                        (username, password, email)
                    )

        db.commit()
        return cursor.lastrowid

    # Get error messages
    except catch_error(), e:
        print "Error %d: %s" % (e.args[0],e.args[1])


    # Close connection
    finally:
        if db:
            db.close()

    return None


def logout():
    """Logout user (delete token)"""

    # Open connection and execute SQL to create new user
    try:
        db, cursor = connect()
        
        cursor.execute("""DELETE FROM tokens
                        WHERE user_id=%s
                        """ % g.user.id
                    )

        db.commit()
        return g.user.id

    # Get error messages
    except catch_error(), e:
        print "Error %d: %s" % (e.args[0],e.args[1])


    # Close connection
    finally:
        if db:
            db.close()

    return None
