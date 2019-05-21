"""
My little Stack
"""

my_stack = []


def push(elem) -> None:
    """
    Operation that add element to stack
    :param elem: element to be pushed
    :return: Nothing
    """
    global my_stack
    my_stack.append(elem)
    return None


def pop():
    """
    Pop element from the top of the stack
    :return: popped element
    """
    global my_stack
    if my_stack == []:
        return None
    else:
        pop_elem = my_stack[-1]
        del my_stack[-1]
        return pop_elem


def peek(ind=0):
    """
    Allow you to see at the element in the stack without popping it
    :param ind: index of element (count from the top)
    :return: peeked element
    """
    global my_stack
    if ind > len(my_stack) - 1:
        return None
    else:
        return my_stack[ind - 1]


def clear() -> None:
    """
    Clear my stack
    :return: None
    """
    global my_stack
    my_stack = []
    return None

