from app.wah import app
from unittest import TestCase
import json
import tempfile


class FlaskTestCase(TestCase):
	"""docstring for FlaskTestCase"""


	def setUp(self):
		self.tester = app.test_client(self)


	# def test_numbers(self):
	# 	r = self.tester.get('/_numbers', content_type="application/json")
	# 	# self.assertEqual(r.status_code, 200)
	# 	self.assertEqual(json.loads(r.data), {"result": 200})

	def test_get_numbers(self):
		r = self.tester.get('/_add_numbers?a=2&b=3', content_type="application/json")
		# self.assertEqual(r.status_code, 200)
		self.assertEqual(json.loads(r.data), {"result": 4})


if __name__ == '__main__':
	unittest.main()
