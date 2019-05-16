from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with bubble sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    for idx, val in enumerate(container):
        changed = False
        for j in range(len(container) - idx - 1):
            if container[j] > container[j + 1]:
                container[j], container[j+1] = container[j+1], container[j]
                changed = True
        if not changed:
            break
    return container
