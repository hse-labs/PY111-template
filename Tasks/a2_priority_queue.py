"""
Priority Queue

Queue priorities are from 0 to 5
"""
priority_queue = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}


def enqueue(elem, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param priority: element priority
    :param elem: element to be added
    :return: Nothing
    """
    global priority_queue
    priority_queue[priority].append(elem)
    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """
    global priority_queue
    for i in range(6):
        if priority_queue[i]:
            elem = priority_queue[i][0]
            del priority_queue[i][0]
            return elem
    return None


def peek(ind: int = 0, priority: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param priority: element priority
    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    global priority_queue
    return priority_queue[priority][ind] if \
        priority_queue[priority][ind] else None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    global priority_queue
    priority_queue = {0: [], 1: [], 2: [], 3: [], 4: [], 5: []}
    return None
