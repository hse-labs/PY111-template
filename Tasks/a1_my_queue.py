"""
My little Queue
"""
q = []


def enqueue(elem) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global q
    q.insert(0, elem)
    return None


def length():
    return len(q)


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """
    global q
    if len(q) > 0:
        dq = q[-1]
        del q[-1]
        return dq
    else:
        return None


def peek(ind: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global q
    if ind < 0:
        return None
    if abs(ind) > len(q):
        return None
    if len(q) - ind - 1 >= 0:
        return q[len(q) - ind - 1]
    else:
        return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global q
    q = []
    return None


if __name__ == "__main__":
    enqueue(1)
    print(q)
    enqueue(2)
    print(q)
    enqueue(3)
    print(q)
    enqueue(4)
    print(q)
    dequeue()
    print(q)
    print(peek(5))
