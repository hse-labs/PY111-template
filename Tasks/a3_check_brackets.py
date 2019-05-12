import Tasks.a0_my_stack as stack


def check_brackets(brackets_row: str) -> bool:
    """
    Check whether input string is a valid bracket sequence
    :param brackets_row: input string to be checked
    :return: True if valid, False otherwise
    """
    for i in brackets_row:
        if i == "(" or i == "{" or i == "[":
            stack.push(i)
        elif i == ")" and (stack.length() == 0 or stack.peek() != "("):
            return False
        elif i == "}" and (stack.length() == 0 or stack.peek() != "{"):
            return False
        elif i == "]" and (stack.length() == 0 or stack.peek() != "["):
            return False
        elif i == ")" and stack.peek() == "(":
            stack.pop()
        elif i == "}" and stack.peek() == "{":
            stack.pop()
        elif i == "]" and stack.peek() == "[":
            stack.pop()

    if stack.length() == 0:
        stack.clear()
        return True
    else:
        stack.clear()
        return False


if __name__ == "__main__":
    brackets_row = "(()))"
    print(check_brackets(brackets_row))
    brackets_row = "()"
    print(check_brackets(brackets_row))
