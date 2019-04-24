"""
My little Stack
"""
some_list = []


def push(elem) -> None:
    """
    Operation that add element to stack

    :param elem: element to be pushed
    :return: Nothing
    """
    global some_list
    some_list.append(elem)
    return None


def pop():
    """
    Pop element from the top of the stack

    :return: popped element
    """
    global some_list
    if len(some_list) > 0:
        first_variable = some_list[-1]
        del some_list[-1]
        return first_variable
    else:
        return None



def peek(ind: int = 0):
    """
    Allow you to see at the element in the stack without popping it

    :param ind: index of element (count from the top)
    :return: peeked element
    """
    global some_list
    try:
        some_variable = some_list[ind]
        print(some_variable)
    except IndexError:
        print(f"элемента с индексом {ind} не существует")
    return None


def clear() -> None:
    """
    Clear my stack

    :return: None
    """
    global some_list
    some_list.clear()
    return None


if __name__ == '__main__':
    push('a')
    push('b')
    push('c')
    pop()
    peek(1)
