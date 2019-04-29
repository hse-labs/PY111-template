def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	b = 0

	for letter in brackets_row:
		if letter == ')':
			b -= 1
			if b < 0 :
				return False
		elif letter == '(':
			b += 1
	return not bool(b)
