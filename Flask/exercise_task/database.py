#!/usr/bin/env python
# -*- coding: utf-8 -*-


import MySQLdb
import MySQLdb.cursors


def connect():
	host = "localhost"
	port = 3306
	user = "root"
	# passwd = "toor"
	db = "flask_tasks"

	# conn = MySQLdb.connect(host=host, port=port, 
	# 					user=user, passwd=passwd, db=db)
	conn = MySQLdb.connect(host=host, port=port, 
						user=user, db=db, 
						cursorclass=MySQLdb.cursors.DictCursor)
	cursor = conn.cursor()
	
	return conn, cursor


def close():
	MySQLdb.close()


def catch_error():
	# Handle error
	return MySQLdb.Error