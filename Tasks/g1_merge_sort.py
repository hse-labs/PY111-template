from typing import Collection, TypeVar
import random

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container
    middle = len(container) // 2
    left = sort(container[:middle])
    right = sort(container[middle:])
    return merge(left, right)


def merge(arr1: Collection[_Tt], arr2: Collection[_Tt]):
    res = []
    while arr1 and arr2:
        if arr1[0] < arr2[0]:
            res.append(arr1.pop(0))
        else:
            res.append(arr2.pop(0))
    else:
        res += list(arr1) if arr1 else list(arr2)
    return res


if __name__ == "__main__":
    arr = [random.randint(-100, 100) for _ in range(30)]
    print(arr)
    print(sort(arr))
