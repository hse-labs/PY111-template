def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n <= 2:
        return 1
    return fib_recursive(n - 1) + fib_recursive(n - 2)


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    fib = 0
    a = 1
    b = 0
    for i in range(n-1):
        fib = a + b
        b = a
        a = fib
    return fib


if __name__ == "__main__":
    print(fib_recursive(8))
    print(fib_iterative(8))
