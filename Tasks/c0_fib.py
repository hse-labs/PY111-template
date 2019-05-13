def fib_recursive(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using recursive algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0 or type(n) == float:
        raise ValueError("Функция определена только для натуральных чисел")
    if n == 0:
        return 0
    if n == 1:
        return 1
    else:
        number = fib_recursive(n-1) + fib_recursive(n-2)
    return number


def fib_iterative(n: int) -> int:
    """
    Calculate n-th number of Fibonacci sequence using iterative algorithm

    :param n: number of item
    :return: Fibonacci number
    """
    if n < 0 or type(n) == float:
        raise ValueError("Функция определена только для натуральных чисел")
    if n == 1:
        return 0
    if n == 2:
        return 1
    first_n, second_n = 0, 1
    number = 0
    for _ in range(2, n+1):
        number = first_n + second_n
        first_n, second_n = second_n, number
    return number
