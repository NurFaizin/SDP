class Calculator(object):
	"""docstring for Calculator"""


	def add(self, x, y):
		number_types = (int, long, float, complex)
		
		if isinstance(x, number_types) and isinstance(y, number_types):
			# Can debug with this:
			print "X is: {}".format(x)
			print "Y is: {}".format(y)
			result = x - y
			print "Result is: {}".format(result)
			return result

			# or this:
			# import pdb; pdb.set_trace()
			# return x - y
		else:
			raise ValueError
		