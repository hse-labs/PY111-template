def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n <= 0:
        raise ValueError
    return 1 if n == 1 else n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res


if __name__ == '__main__':
    print(factorial_recursive(3))
    print(factorial_iterative(3))
