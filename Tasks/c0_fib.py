def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n == 1:
        return 1
    elif n == 0:
        return 0
    elif n < 0:
        raise ValueError
    return fib_recursive(n - 2) + fib_recursive(n - 1)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    a, b = 0, 1
    for i in range(n-1):
        a, b = b, a + b
    if n < 0:
        raise ValueError
    return b


if __name__ == '__main__':
    print(fib_recursive(-2))
    print(fib_iterative(-2))
