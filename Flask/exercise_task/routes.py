#!/usr/bin/env python
# -*- coding: utf-8 -*-


from flask import g, Blueprint, jsonify, request, Response
import re
from flask.ext.login import current_user, login_required
import tasks, users, error_handlers


blueprint = Blueprint('tasks', __name__)


@blueprint.before_request
def before_request():
	"""Set global user"""
	g.user = current_user


@blueprint.route('/')
def index():
	return "Hello Tasks!"


@blueprint.route("/login", methods=["POST"])
@login_required
def login():
    access_token, secret_token = users.generate_token()
    data = {
                'status': 200,
                'message': "Login success!",
                'data': 'Hello, %s!' % g.user.username,
                'secret_token': secret_token,
                'access_token': access_token
            }
    return jsonify(data)


@blueprint.route('/logout', methods=['POST'])
@login_required
def logout():
	resp_data = {}
	if users.logout():
		resp_data = {
		            'status': 200,
		            'message': "Logout success!",
		        }
	
	return jsonify(resp_data)


@blueprint.route('/users', methods=['POST'])
@login_required
def create_user():
	"""Route for create new user (register)"""

	user_data = {
		'username': request.form.get('username'),
		'password': request.form.get('password'),
		'email': request.form.get('email')
	}

	# Input validation
	# Regex pattern
	username_criteria = "^[a-zA-Z0-9_]{3,35}$"

	# Check if any field is null
	required = []
	for key, value in user_data.iteritems():
		if not value:
			required.append(key)

	if required:  # If any field is null
		return error_handlers.bad_request( (",").join(required) + " required")

	else:  # No one field is null

		# Check criteria
		if not re.search(username_criteria, user_data['username']):
			return error_handlers.bad_request(
				"Username must between 3-35 characters and "
				"can contain only [a-z] [A-Z] [0-9] and " 
				"undescore '_' "
				)

		elif len(user_data['password']) < 6:
			return error_handlers.bad_request("Password must have 6 characters")

		else:  # Input valid
			# Try create new user
			new_user_id = users.create_user(user_data)
			response={}
			
			if new_user_id:  # If success create new user
				links = '%s/%s' % (request.url, new_user_id)
				response['data'] = {
						'id' : new_user_id,
				        'type': 'users',
				        'attributes': user_data,
				        'links' : {
				        	'self': links
				        }
				}
				status = 201
			else:  # If failed create new user
				status = 202

			resp = jsonify(response)

			# Header JSONAPI
			resp.mimetype = 'application/vnd.api+json'  
			resp.location = links
			resp.status_code = status

			return resp


@blueprint.route('/tasks', methods=['GET'])
@login_required
def get_tasks():
	"""Route for get all tasks"""

	if request.args.get('keyword'):
		keyword = request.args.get('keyword')
		tasks_data = tasks.get_tasks_many(keyword)
	else:
		tasks_data = tasks.get_tasks()
	
	resp_data = []
	if tasks_data:
		for task in tasks_data:
			
			# Get task attribute except 'id' and 'user_id'
			attributes = { 
				k:v for k,v in task.iteritems() 
				if k not in('id', 'user_id') 
			}

			resp_data.append({
					'type': 'tasks',
					'id': task['id'],
					'attributes': attributes
				})

	response = {
		'links': { 'self': request.url },
		'data' : resp_data
	}
	resp = jsonify(response)

	# Header JSONAPI
	resp.mimetype = 'application/vnd.api+json'  
	resp.status_code = 200

	return resp


@blueprint.route('/tasks/<int:id>', methods=['GET'])
@login_required
def get_task_by_id(id):
	"""Route for create get a task"""

	task = tasks.get_task_by_id(id)

	response={}	
	if task:
		links = request.url
		# Get task data except 'id' and 'user_id'
		task_data = { 
			k:v for k,v in task.iteritems() 
			if k not in('id', 'user_id') 
		}

		response['data'] = {
				'id' : task['id'],
		        'type': 'tasks',
		        'attributes': task_data,
		        'links' : {
		        	'self': links
		        }
		}

	else:
		return error_handlers.not_found()

	resp = jsonify(response)
	resp.status_code = 200

	return resp


@blueprint.route('/tasks', methods=['POST'])
@login_required
def create_task():
	"""Route for create new task"""

	# Get form data
	task_data = {
		'user_id': request.form.get('user_id'),
		'description': request.form.get('description'),
		'due_date': request.form.get('due_date'),
		'priority': request.form.get('priority')
	}

	# Input validation
	# Check if any field is null
	required = []
	for key, value in task_data.iteritems():
		if not value:
			required.append(key)

	if required:  # If any field is null
		return error_handlers.bad_request( (",").join(required) + " required")
	
	else:  # Input valid

		new_task_id = tasks.create_task(task_data)
		response={}
		
		if new_task_id:
			links = '%s/%s' % (request.url, new_task_id)
			response['data'] = {
					'id' : new_task_id,
			        'type': 'tasks',
			        'attributes': task_data,
			        'links' : {
			        	'self': links
			        }
			}
			status = 201
		else:
			status = 202

		resp = jsonify(response)

		# Header JSONAPI
		resp.mimetype = 'application/vnd.api+json'  
		resp.location = links
		resp.status_code = status

		return resp


@blueprint.route('/tasks/<int:id>', methods=['PUT'])
@login_required
def update_task(id):

	task_data = {
		'id' : id,
		'user_id': request.form.get('user_id'),
		'description': request.form.get('description'),
		'due_date': request.form.get('due_date'),
		'priority': request.form.get('priority')
	}

	# Input validation
	# Check if any field is null
	required = []
	for key, value in task_data.iteritems():
		if not value:
			required.append(key)

	if required:  # If any field is null
		return error_handlers.bad_request( (",").join(required) + " required")
	
	else:  # Input valid

		updated_task_id = tasks.update_task(task_data)
		
		if updated_task_id:  # Update success

			# Get task was updated
			task = tasks.get_task_by_id(updated_task_id)

			response={}

			links = request.url
			# Get task data except 'id' and 'user_id'
			task_data = { 
				k:v for k,v in task.iteritems() 
				if k not in('id', 'user_id') 
			}

			response['data'] = {
					'id' : task['id'],
			        'type': 'tasks',
			        'attributes': task_data,
			        'links' : {
			        	'self': links
			        }
			}

		else:  # Update failed
			return error_handlers.not_found()

		resp = jsonify(response)

		# Header JSONAPI
		resp.mimetype = 'application/vnd.api+json'  
		resp.location = links
		resp.status_code = 200

		return resp


@blueprint.route('/tasks/<int:id>', methods=['PATCH'])
@login_required
def update_task_status(id):
	
	status = request.form.get('status')

	if not status:
		return error_handlers.bad_request("status required")

	updated_task_id = tasks.update_task_status(id, status)
	
	if updated_task_id: # Update success

		# Get task was updated
		task = tasks.get_task_by_id(updated_task_id)

		response={}

		links = request.url
		# Get task data except 'id' and 'user_id'
		task_data = { 
			k:v for k,v in task.iteritems() 
			if k not in('id', 'user_id') 
		}

		response['data'] = {
				'id' : task['id'],
		        'type': 'tasks',
		        'attributes': task_data,
		        'links' : {
		        	'self': links
		        }
		}

	else:  # Update failed
		return error_handlers.not_found()

	resp = jsonify(response)

	# Header JSONAPI
	resp.mimetype = 'application/vnd.api+json'  
	resp.location = links
	resp.status_code = 200

	return resp


@blueprint.route('/tasks/<ids>', methods=['DELETE'])
@login_required
def delete_tasks(ids):

	ids = ids.split(',')

	if len(ids) >= 1:
		if tasks.delete_tasks(ids):
			response = {
			        'meta': {
			        	'author': 'Nur Faizin'
			        }
			}
			status = 200
		else:
			return error_handlers.internal_error()


	resp = jsonify(response)
	resp.status_code = status

	return resp

