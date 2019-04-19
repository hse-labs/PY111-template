"""
My little Stack
"""

somelist = []


def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global somelist
	somelist.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global somelist
	if len(somelist) > 0:
		return somelist.pop()
	else:
		pass


def peek(ind: int = 0):

	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global somelist
	return somelist[ind - 1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global somelist
	somelist = []
	return None
