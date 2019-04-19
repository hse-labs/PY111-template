"""
My little Stack
"""
a = []


def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	a.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global a
	if len(a) == 0:
		return None
	else:
		result = a[-1]
	del a[-1]
	return result


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global a
	for i in a:
		if i < 0:
			return None
		else:
			return a[-1-ind]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global a
	return None
