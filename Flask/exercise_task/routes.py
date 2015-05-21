#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import Flask, jsonify, request, Blueprint
from database import Database

tasks = Blueprint('tasks', __name__)


@tasks.route('/')
def index():
	return "Hello Tasks!"


@tasks.route('/register', methods=['POST'])
def register():
	username = request.form['username']
	password = request.form['password']
	email = request.form['email']

	pass


@tasks.route('/login', methods=['POST'])
def login():
	pass


@tasks.route('/logout', methods=['POST'])
def logout():
	pass


@tasks.route('/tasks', methods=['GET'])
def get_tasks():
	pass


@tasks.route('/tasks', methods=['POST'])
def create_task():
	pass


@tasks.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id():
	pass


@tasks.route('/tasks/<int:id>', methods=['GET'])
def get_task_by_id():
	pass


@tasks.route('/tasks/<string:keyword>', methods=['GET'])
def get_task_by_keyword():
	pass


@tasks.route('/tasks/delete/<ids>', methods=['DELETE'])
def del_task_by_ids():
	pass





@tasks.route('/task/update/<int:id>', methods=['PUT'])
def get_task():
	pass
