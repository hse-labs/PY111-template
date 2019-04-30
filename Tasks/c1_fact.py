import math


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
    ftrl = factorial_recursive(n - 1) * n
    return ftrl


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 0:
        raise ValueError
    ftrl = 1
    for i in range(1, n + 1):
        ftrl *= i
    return ftrl
