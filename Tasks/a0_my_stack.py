"""
My little Stack
"""

my_stack = []


def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	my_stack.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	if my_stack:
		return my_stack.pop()
	else:
		return None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	return my_stack[ind - 1]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	my_stack.clear()
	return None
