from typing import Collection, TypeVar
import random

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
    """
    Sort input container with quick sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    if len(container) <= 1:
        return container
    else:
        base = container[random.randint(0, len(container) - 1)]
    # left = [i for i in container if i < base]
    # right = [i for i in container if i > base]
    # mid = [i for i in container if i == base]
    # return sort(left) + mid + sort(right)
    left = []
    right = []
    mid = []
    for i in container:
        if i < base:
            left.append(i)
        elif i > base:
            right.append(i)
        else:
            mid.append(i)
    return sort(left) + mid + sort(right)

    # l_cnt = 0
    # r_cnt = len(container) - 1
    # while l_cnt < r_cnt:
    #     while container[l_cnt] < base:
    #         l_cnt += 1
    #     while container[r_cnt] > base:
    #         r_cnt -= 1
    #     if l_cnt == 0 and r_cnt == len(container) - 1:
    #         return container
    #     container[l_cnt], container[r_cnt] = container[r_cnt], container[l_cnt]
    # else:
    #     par = l_cnt
    # return sort(container[:par]) + sort(container[par:])


if __name__ == '__main__':
    # arr = [random.randint(-100, 100) for _ in range(10)]
    arr = {1: 4, 2: 4, 3: 4, 1: 5, -4: 4, -5: 4, 4: 0}
    print(arr)
    print(sort(arr))
