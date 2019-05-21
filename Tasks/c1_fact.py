def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""
	try:
		assert n >= 1
	except AssertionError:
		raise ValueError
	if n == 1:
		return 1
	else:
		return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way

	:param n: int > 0
	:return: factorial of n
	"""
	try:
		assert n >= 1
	except AssertionError:
		raise ValueError
	factorial = 1
	while n > 1:
		factorial *= n
		n -= 1
	return factorial
