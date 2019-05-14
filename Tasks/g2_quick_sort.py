from typing import Sequence, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) < 1:
        return container
    index = round(len(container) // 2)
    left = 0
    right = len(container) - 1
    op = container[index]
    while left < right:
        while container[left] <= op:
            left += 1
        while container[right] > op:
            right -= 1
        if left < right:
            container[left], container[right] = container[right], container[left]

    a = container[0:left]
    b = container[left:]
    a1 = sort(a)
    b1 = sort(b)
    container = a1 + b1
    return container


if __name__ == "__main__":
    cont = [5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10]
    print(sort(cont))
