

def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    s = 0
    d = 0
    for i in brackets_row:
        if i == '(':
            s += 1
        if i == ')':
            d += 1
    return False if s != d else True


