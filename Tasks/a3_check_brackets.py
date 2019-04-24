def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """

    s = 0
    for i in brackets_row:
        if i == '(':
            s += 1
        else:
            s -= 1
            if s <= -1:
                return False
    return False if s != 0 else True
