"""
My little Stack
"""
stak = []


def push(elem) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    stak.append(elem)


def pop():
    """
    Pop element from the top of the stack

    :return: popped element
    """
    if stak == []:
        return None
    else:
        return stak.pop()


def peek(ind: int = 0):
    """
        Allow you to see at the element in the stack without popping it

        :param ind: index of element (count from the top)
        :return: peeked element
        """
    try:

        s = stak[ind - 1]
    except IndexError:
        return None
    else:
        return s


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    stak.clear()
    return None
