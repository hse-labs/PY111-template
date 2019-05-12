"""
Priority Queue

Queue priorities are from 0 to 5
"""
q = [[], [], [], [], [], []]


def enqueue(elem, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """

    global q
    q[priority].insert(0, elem)
    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """
    global q
    qq = None
    for i in range(5, 0, -1):
        if q[i]:
            qq = q[i][-1]
            del q[i][-1]
            break
    return qq


def peek(ind: int = 0, priority: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global q
    qq = q[priority]
    return qq[ind]


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global q
    q = [[], [], [], [], [], []]
    return None


if __name__ == "__main__":
    enqueue(0, 0)
    enqueue(11, 1)
    enqueue(22, 2)
    enqueue(23, 2)
    print(q)
    print(len(q[2]))
    print(peek(0, 1))
    print(dequeue())
    print(q)
    clear()
    print(q)
