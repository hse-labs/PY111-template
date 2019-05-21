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
    a = 1

    for i in range(1, 100):
        a += (x ** i) / math.factorial(i)

    return a


def sinx(x) -> float:
    """
    Calculate sin(x) with Taylor series
    :param x: x value
    :return: sin(x) value
    """
    b = x

    for i in range(1, 10):
        if i % 2 == 1:
            b -= x ** (2 * i + 1) / math.factorial(2 * i + 1)
        else:
            b += x ** (2 * i + 1) / math.factorial(2 * i + 1)
    return b
