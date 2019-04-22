"""
My little Queue
"""
stak = []


def enqueue(elem) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    return stak.append(elem)


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """
    if stak is not None:
        point = stak[0]
        del stak[0]
        return point
    else:
        return None


def peek(ind: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """

    # try:
    #    s = stak.index(stak[ind])
    # except(IndexError,ValueError):
    #     return None

    if stak is not None:
        return stak[ind] if stak[ind] else None
    #     return stak.index(stak[ind])


def clear() -> None:
    """
    Clear my queue

    :return: None
    """

    return stak.clear()
