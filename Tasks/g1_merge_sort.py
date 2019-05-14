from typing import TypeVar

_Tt = TypeVar("_Tt")


def sort(container):
    """
    Sort input container with merge sort

    :param container: container of elements to be sorted
    :return: container sorted in ascending order
    """
    def mrg(cont1, cont2):
        c = []
        while cont1 and cont2:
            if cont1[0] > cont2[0]:
                c.append(cont2[0])
                del cont2[0]
            else:
                c.append(cont1[0])
                del cont1[0]
        c += cont1 + cont2
        return c

    if len(container) <= 1:
        return container
    d = round(len(container) // 2)
    a = sort(container[:d])
    b = sort(container[d:])
    c1 = mrg(a, b)
    return c1


if __name__ == "__main__":
    cont = [5, 4, 6, 3, 7, 2, 8, 1, 9, 0, 10]
    print(sort(cont))
