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

	fact = n
	if n == 1:
		return 1
	else:
		return fact*factorial_recursive(n-1)


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
	fact = 1
	for i in range(1, n+1):
		fact *= i
	return fact

