from typing import Sequence, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for j in range(len(container) - 1):
        b = True
        for i in range(len(container) - 1 - j):
            if container[i] > container[i + 1]:
                container[i], container[i + 1] = container[i + 1], container[i]
                b = False
        if b:
            return container
    return container


if __name__ == "__main__":
    cont = [5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10]
    print(sort(cont))
