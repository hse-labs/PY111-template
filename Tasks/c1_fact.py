def factorial_recursive(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in recursive way
	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError
	else:
		if n in (0, 1):
			return 1
		else:
			return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
	"""
	Calculate factorial of number n (> 0) in iterative way

	:param n: int > 0
	:return: factorial of n
	"""
	if n < 0:
		raise ValueError
	else:
		fact = 1
		i = 1
		while i < n:
			fact += fact * i
			i += 1
	return fact
