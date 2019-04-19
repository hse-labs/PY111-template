"""
My little Stack
"""

stack = []


def push(elem) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global stack
    stack.append(elem)
    return None


def pop():
    """
    Pop element from the top of the stack

    :return: popped element
    """
    global stack
    if len(stack) == 0:
        print('empty stack')
        return None
    else:
        top_element = stack[-1]
        del stack[-1]
    return top_element


def peek(ind: int = 0):
    """
    Allow you to see at the element in the stack without popping it

    :param ind: index of element (count from the top)
    :return: peeked element
    """
    global stack
    index = len(stack) - 1 - ind
    if not stack[index]:
        return None
    else:
        return stack[index]


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global stack
    stack = []
    return None


if __name__ == '__main__':
    push('test1')
    push('test2')
    print(stack)
    print(pop())
    print(peek(0))
