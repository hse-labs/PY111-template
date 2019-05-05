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
    res = 1
    fact = 1
    for i in range(1, 50):
        fact *= i
        res += x ** i / fact
    return res


def sinx(x) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    fact = 1
    x = x % (2 * math.pi)
    res = x
    for i in range(1, 85):
        fact *= 2 * i * (2 * i + 1)
        res += (-1) ** i * x ** (2 * i + 1) / fact
    return res


if __name__ == '__main__':
    print(math.sin(1000))
    print(sinx(1000))
