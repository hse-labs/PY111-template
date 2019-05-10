def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	brackets_type = set(brackets_row)
	brackets_type = sorted(brackets_type)
	opening, closing = brackets_type[::2], brackets_type[1::2]
	stack = []
	for i in brackets_row:
		if i in opening:
			stack.append(opening.index(i))
		elif i in closing:
			if stack and stack[-1] == closing.index(i):
				stack.pop()
			else:
				return False
	return not stack
