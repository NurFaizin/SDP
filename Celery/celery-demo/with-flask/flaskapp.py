# -*- coding: utf8 -*-
from flask import Flask, request, jsonify
from celery_factory import create_celery
from actionholder import kirim


app = Flask("flaskCelery", "/")


@app.route("/")
def index():
    data = {
        "code": 200,
        "message": "welcome to flaskCelery demo"
    }
    return jsonify(data)


@app.route("/sendmail", methods=['POST'])
def send_mail():

    kirim(request.form)

    return jsonify({
        "code": 200,
        "message": "sent"
    })


#: bind celery ke flask
flask_celery = create_celery(app)
