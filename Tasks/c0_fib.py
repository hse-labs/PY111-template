def fib_recursive(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using recursive algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	if n == 1:
		return 1
	if n < 1:
		return 0
	return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
	"""
	Calculate n-th number of Fibonacci sequence using iterative algorithm

	:param n: number of item
	:return: Fibonacci number
	"""
	a = 0
	b = 1
	next_item = 0
	for i in range(3, n+1):
		next_item = a + b
		a = b
		b = next_item
	return next_item


if __name__ == '__main__':
	print(fib_iterative(7))
