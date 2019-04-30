def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if type(n) != int:
        raise ValueError

    if n < 1:
        return 0
    if n == 1:
        return 1
    fib_re = fib_recursive(n - 1) + fib_recursive(n - 2)
    return fib_re


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0:
        raise ValueError
    if type(n) != int:
        raise ValueError
    a = 0
    d = 1
    fib_it = 0

    for i in range(0, n - 1):
        fib_it = a + d
        a = d
        d = fib_it
    return fib_it
