"""
My little Stack
"""
stack = []


def push(elem) -> None:
	"""
	Operation that add element to stack
	:param elem: element to be pushed
	:return: Nothing
	"""
	global stack
	stack.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global stack
	return stack.pop() if len(stack) > 0 else None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global stack
	return stack[len(stack) - 1 - ind]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global stack
	stack.clear()
	return None


if __name__ == '__main__':
	push('vetka')
	push('vetka')
	print(stack)
	print(pop())
	print(peek(0))

