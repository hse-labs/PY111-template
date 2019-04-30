"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """

    a = 0
    b = 0
    for i in range(len(arr)):
        # print(arr[i])
        if arr[i] < a:
            a = arr[i]
            b = i
    return b
