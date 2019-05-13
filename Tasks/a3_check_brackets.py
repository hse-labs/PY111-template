def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    brackets_stack = []
    brackets_dict = {'(': ')', '{': '}', '[': ']'}
    for i in brackets_row:
        if i in brackets_dict:
            brackets_stack.append(i)
        else:
            try:
                op_bracket = brackets_stack.pop()
                assert brackets_dict[op_bracket] == i
            except (IndexError, AssertionError):
                return False
    if not brackets_stack:
        return True
    else:
        return False
