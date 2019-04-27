def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	brackets_stack = []
	brackets_dict = {')': '(', '}': '{', ']': '['}
	for i in brackets_row:
		if i not in [')', '(', '}', '{', ']', '[']:
			continue
		if i in brackets_dict.values():
			brackets_stack.append(i)
		elif i in brackets_dict.keys():
			try:
				assert brackets_stack.pop() == brackets_dict[i]
			except (IndexError, AssertionError):
				return False
	if not brackets_stack:
		return True
	else:
		return False

