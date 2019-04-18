def check_brackets(brackets_row: str) -> bool:
	"""
	Check whether input string is a valid bracket sequence
	:param brackets_row: input string to be checked
	:return: True if valid, False otherwise
	"""
	brackets = {'(': 0, ')': 0}
	for chr_ in brackets_row:
		if chr_ == '(' or (chr_ == ')' and brackets[chr_] <= brackets['(']):
			brackets[chr_] += 1
	return True if brackets['('] == brackets[')'] else False


# def check_brackets(brackets_row: str) -> bool:
# 	"""
# 	Check whether input string is a valid bracket sequence
# 	:param brackets_row: input string to be checked
# 	:return: True if valid, False otherwise
# 	"""
# 	brackets = {'(':0, ')':0}
# 	for chr in brackets_row:
# 		if chr == '(':
# 			brackets[chr] += 1
# 		elif chr == ')' and brackets[chr] <= brackets['(']:
# 			brackets[chr] += 1
# 	return True if brackets['('] == brackets[')'] else False
