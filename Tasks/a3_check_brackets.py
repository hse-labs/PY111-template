def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	x = 0
	for c in brackets_row:
		if c == '(':
			x += 1
		elif c == ')':
			x -= 1
			if x < 0:
				return False
			elif x == 0:
				return True
