def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""

	if n < 0 or type(n) == float:
		raise ValueError

	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 0:
		return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""

	if n < 0 or type(n) == float:
		raise ValueError

	fib1 = 1
	fib2 = 1
	i = 0

	if n == 0:
		return 0
	elif n == 1:
		return 1
	elif n > 0:
		while i < n - 2:
			fib_sum = fib1 + fib2
			fib1 = fib2
			fib2 = fib_sum
			i = i + 1

		return fib2
