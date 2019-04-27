"""
Taylor series
"""


def ex(x) -> float:
	"""
	Calculate value of e^x with Taylor series

	:param x: x value
	:return: e^x value
	"""
	ans = 1
	fact = 1
	for i in range(1, 10):
		fact *= i
		ans += x**i/fact
	return ans


def sinx(x) -> float:
	"""
	Calculate sin(x) with Taylor series

	:param x: x value
	:return: sin(x) value
	"""
	ans = x
	fact = 1
	for i in range(1, 15):
		fact *= 2*i * (2*i + 1)
		ans += (-1)**i * x ** (2*i + 1) / fact
	return ans
