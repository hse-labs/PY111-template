"""
Taylor series
"""
import math


def ex(x) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    total_series = 1

    for i in range(1, 100):
        total_series += (x ** i) / math.factorial(i)

    return total_series


def sinx(x) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    total_series = x

    for i in range(1, 10):
        if i % 2 == 1:
            total_series -= x ** (2 * i + 1) / math.factorial(2 * i + 1)
        else:
            total_series += x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return total_series


if __name__ == '__main__':
    print(ex(5))
