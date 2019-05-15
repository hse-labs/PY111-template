def factorial_recursive(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in recursive way
    :param n: int > 0
    :return: factorial of n
    """
    if n < 1:
        raise ValueError("Функция определена только для натуральных чисел")
    if n == 1:
        return 1
    else:
        return n * factorial_recursive(n - 1)


def factorial_iterative(n: int) -> int:
    """
    Calculate factorial of number n (> 0) in iterative way

    :param n: int > 0
    :return: factorial of n
    """
    if n < 1:
        raise ValueError("Функция определена только для натуральных чисел")
    fact = 1
    for i in range(2, n + 1):
        fact *= i
    return fact
