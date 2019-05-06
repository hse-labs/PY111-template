def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError

	if n == 0:
		return 1
	elif n == 1:
		return 1
	elif n > 1:
		return factorial_recursive(n - 1) * n


def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way

	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError

	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 1:
		result = 1
		while n >= 1:
			result *= n
			n = n - 1
		return result
