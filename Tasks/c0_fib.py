def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm
	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0 or type(n) == float:
		raise ValueError
	if n < 3:
		return 1
	return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm
	:param n: number of item
	:return: Fibonacci number
	"""
	if n < 0 or type(n) == float:
		raise ValueError
	global fib_sum
	fib1 = fib2 = 1
	i = 2
	while i < n:
		fib_sum = fib2 + fib1
		fib1 = fib2
		fib2 = fib_sum
		i += 1
	return fib_sum
