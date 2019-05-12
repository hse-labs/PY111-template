"""
Taylor series
"""


def ex(x) -> float:
    """
    Calculate value of e^x with Taylor series

    :param x: x value
    :return: e^x value
    """
    e = 1
    fact = 1
    for i in range(1, 10):
        fact *= i
        e += x ** i / fact
    return e


def sinx(x) -> float:
    """
    Calculate sin(x) with Taylor series

    :param x: x value
    :return: sin(x) value
    """
    sx = x
    z = -1
    fact = 2
    for i in range(3, 10):
        fact *= i
        if i % 2 == 1:
            sx += z * x ** i / fact
            z *= -1
    return sx


if __name__ == "__main__":
    print(ex(22))
    print(sinx(22))
