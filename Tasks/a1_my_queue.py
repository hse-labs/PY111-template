"""
My little Queue
"""
queue = []


def enqueue(elem) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    global queue
    queue.append(elem)
    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """
    global queue
    if queue:
        elem = queue[0]
        del queue[0]
        return elem
    else:
        return None


def peek(ind: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    return queue[ind] if queue[ind] else None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global queue
    queue.clear()
    return None
