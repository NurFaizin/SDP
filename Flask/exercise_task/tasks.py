#!/usr/bin/env python
# -*- coding: utf-8 -*-


from database import connect, catch_error


def get_tasks():
	"""Get all tasks"""

	# Open connection and execute SQL to get all tasks
	try:
		db, cursor = connect()
		cursor.execute("""SELECT * FROM tasks""")

		tasks = cursor.fetchall()

	# Get error messages
	except catch_error(), e:
		print "Error %d: %s" % (e.args[0],e.args[1])

	# Close connection
	finally:
		if db:
			db.close()

	return tasks


def get_tasks_many(keyword):
	"""Get many tasks"""

	# Open connection and execute SQL to get many tasks
	try:
		db, cursor = connect()
		
		cursor.execute("""SELECT * FROM tasks 
						WHERE description LIKE %s""", ("%" + keyword + "%",))

		tasks = cursor.fetchall()

	# Get error messages
	except catch_error(), e:
		print "Error %d: %s" % (e.args[0],e.args[1])

	# Close connection
	finally:
		if db:
			db.close()

	return tasks


def get_task_by_id(id):
	"""Get a task by id"""

	# Open connection and execute SQL to get a task
	try:
		db, cursor = connect()
		
		cursor.execute("""SELECT * FROM tasks 
						WHERE id=%s""" % id)

		task = cursor.fetchone()

	# Get error messages
	except catch_error(), e:
		print "Error %d: %s" % (e.args[0],e.args[1])

	# Close connection
	finally:
		if db:
			db.close()

	return task


def check_task_id(id):
	"""Check task existence by id"""

	# Open connection and execute SQL to get a task
	try:
		db, cursor = connect()
		
		cursor.execute("""SELECT id FROM tasks 
						WHERE id=%s""" % id)

		task = cursor.fetchone()

	# Get error messages
	except catch_error(), e:
		print "Error %d: %s" % (e.args[0],e.args[1])

	# Close connection
	finally:
		if db:
			db.close()

	return task


def create_task(task_data):
	"""Create new task"""

	user_id = int(task_data["user_id"])
	description = task_data["description"]
	due_date = int(task_data["due_date"])
	priority = int(task_data["priority"])

	# Open connection and execute SQL to create new task
	try:
		db, cursor = connect()
		
		cursor.execute("""INSERT INTO tasks
						(user_id, description, due_date, priority)
						VALUES (%s, %s, %s, %s)
						""",
						(user_id, description, due_date, priority)
					)

		db.commit()

	# Get error messages
	except catch_error(), e:
		print "Error %d: %s" % (e.args[0],e.args[1])


	# Close connection
	finally:
		if db:
			db.close()

	return cursor.lastrowid


def update_task(task_data):
	"""Update a task"""

	id = int(task_data["id"])
	user_id = int(task_data["user_id"])
	description = task_data["description"]
	due_date = int(task_data["due_date"])
	priority = int(task_data["priority"])

	if check_task_id(id):  # If task id exist
		# Open connection and execute SQL to update a task
		try:
			db, cursor = connect()
			
			cursor.execute("""UPDATE tasks 
							SET 
								user_id=%s, 
								description=%s, 
								due_date=%s, 
								priority=%s
							WHERE
								id=%s
							""",
							(user_id, description, due_date, priority, id)
						)

			db.commit()

		# Get error messages
		except catch_error(), e:
			print "Error %d: %s" % (e.args[0],e.args[1])


		# Close connection
		finally:
			if db:
				db.close()

		return id

	else:  # If task id not exist
		return None


def update_task_status(id, status):
	"""Update task status"""

	id = int(id)

	if check_task_id(id):  # If task id exist
		# Open connection and execute SQL to update task status
		try:
			db, cursor = connect()
			
			cursor.execute("""UPDATE tasks 
							SET 
								status=%s
							WHERE
								id=%s
							""", (status, id)
						)

			db.commit()
			result = True

		# Get error messages
		except catch_error(), e:
			result = False
			print "Error %d: %s" % (e.args[0],e.args[1])


		# Close connection
		finally:
			if db:
				db.close()

		return id
		
	else:
		return None


def delete_tasks(ids):
	"""Delete task(s)"""

	ids = (",").join(ids)

	# Open connection and execute SQL to delete task(s)
	try:
		db, cursor = connect()
		
		cursor.execute("""DELETE FROM tasks 
						WHERE id IN(%s)
						""" % ids
					)

		db.commit()
		result = True

	# Get error messages
	except catch_error(), e:
		result = False
		print "Error %d: %s" % (e.args[0],e.args[1])


	# Close connection
	finally:
		if db:
			db.close()

	return result