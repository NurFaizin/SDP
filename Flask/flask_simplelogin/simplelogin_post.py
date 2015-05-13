#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, Response
from flask.ext.login import LoginManager, UserMixin, login_required


app = Flask(__name__)
login_manager = LoginManager()
login_manager.init_app(app)


class User(UserMixin):
	"""docstring for user"""


	user_dict = {"JohnDoe": ("JohnDoe", "John"),
				"JaneDoe": ("JaneDoe", "Jane")}


	def __init__(self, username, password):
		self.id = username
		self.password = password


	@classmethod
	def get(cls, id):
		return cls.user_dict.get(id)


@login_manager.request_loader
def load_user(request):
	username = request.form['username']
	password = request.form['password']

	if username and password:
		user_entry = User.get(username)
		if (user_entry is not None):
			user = User(user_entry[0], user_entry[1])
			if user.password == password:
				return user
	return None


@app.route('/', methods=["GET"])
def index():
	return Response(response="Hello World!", status=200)


@app.route('/protected', methods=['POST'])
@login_required
def protected():
	return Response(response='Hello protected world!', status=200)


if __name__ == '__main__':
	app.config['SECRET_KEY'] = 'ITSASECRET'
	app.run(debug=True)