"""
My little Queue
"""
stak = []

def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	return stak[max(stak)].append(elem)


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	return None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	return None
