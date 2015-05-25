#!/usr/bin/env python
# -*- coding: utf-8 -*-


import MySQLdb
import MySQLdb.cursors


def db_connect():
    host = "localhost"
    port = 3306
    user = "root"
    # passwd = "passwd"
    db = "test"

    conn = MySQLdb.connect(host=host, port=port, 
    	                    user=user, db=db)

    cursor = conn.cursor()
    
    return conn, cursor 