"""
My little Stack
"""
stek = []


def length():
	return len(stek)


def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global stek
	stek.append(elem)
	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global stek
	if len(stek) != 0:
		r = stek[-1]
		del stek[-1]
		return r
	else:
		return None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global stek
	if len(stek) - ind - 1 >= 0:
		ind = len(stek) - ind - 1
	return stek[ind]


def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global stek
	stek = []
	return None


if __name__ == "__main__":
	print(pop())
	push("push")
	print(stek)
	print(peek(0))
	print(pop())
	print(stek)
	print(clear())
