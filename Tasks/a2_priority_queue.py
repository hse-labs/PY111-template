"""
Priority Queue

Queue priorities are from 0 to 5
"""
test_dict = [[], [], [], [], [], []]


def enqueue(elem, priority: int = 0) -> None:
    """
    Operation that add element to the end of the queue

    :param elem: element to be added
    :return: Nothing
    """
    test_dict[priority].append(elem)
    return None


def dequeue():
    """
    Return element from the beginning of the queue

    :return: dequeued element
    """

    for i in range(6):
        if test_dict[i] != []:
            elem = test_dict[i][0]
            del test_dict[i][0]
            return elem


def peek(ind: int = 0, priority: int = 0):
    """
    Allow you to see at the element in the queue without dequeuing it

    :param ind: index of element (count from the beginning)
    :return: peeked element
    """
    try:
            return test_dict[priority][ind]
    except IndexError:
        return None


def clear() -> None:
    """
    Clear my queue

    :return: None
    """
    for i in range(6):
        if test_dict[i] != []:
            test_dict[i].clear()
    return None
