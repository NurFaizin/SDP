import MySQLdb
import MySQLdb.cursors

class Database(object):
	def __init__(self):
		self.host = "localhost"
		self.port = 3306
		self.user = "root"
		self.passwd = "toor"
		self.db = "test"

	def connect(self):
		conn = MySQLdb.connect(host='localhost', port=3306, 
                    user='root', passwd='toor', db='test')
		cursor = conn.cursor()
		
		return conn, cursor