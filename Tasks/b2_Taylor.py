"""
Taylor series
"""


import math


def ex(x: float) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	n = 0
	res_sum = 0
	while n <= 100:
		res = (x ** n) / (math.factorial(n))
		res_sum += res
		n += 1
	return res_sum


def sinx(x) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	n = 0
	res_sum = 0
	while n <= 20:
		res = (((-1) ** n) * (x ** ((2 * n) + 1) / (math.factorial((2 * n) + 1))))
		res_sum += res
		n += 1
	return res_sum
