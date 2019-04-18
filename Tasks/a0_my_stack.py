"""
My little Stack
"""
l = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global l
	l.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global l
	if l == []:
		return None
	y = l[-1]
	del l[-1]
	return y


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return l[-ind-1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global l
	l.clear()

	return None
