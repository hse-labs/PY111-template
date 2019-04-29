from math import factorial
"""
Taylor series
"""


def ex(x) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""

	ex_ = 1
	n = 1
	for value in range(10):
		ex_ += (x ** n) / factorial(n)
		n += 1
	return float(ex_)


def sinx(x) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	sinx_ = x
	n = 3
	y = 1
	for value in range(10):
		sinx_ += - y * (x ** n)/factorial(n)
		y *= - 1
		n += 2

	return sinx_
