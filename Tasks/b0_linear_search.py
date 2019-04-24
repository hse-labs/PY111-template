"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
    """
    Function that find minimal element in array

    :param arr: Array containing numbers
    :return: index of first occurrence of minimal element in array
    """
    min_idx = 0
    min_ = arr[min_idx]
    for idx, item in enumerate(arr):
        if item < min_:
            min_ = item
            min_idx = idx
    return min_idx

