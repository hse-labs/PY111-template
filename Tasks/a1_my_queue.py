"""
My little Queue
"""

my_enqueue = []


def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	if my_enqueue is not None:
		my_enqueue.append(elem)


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if my_enqueue:
		return my_enqueue.pop(0)


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return my_enqueue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	if my_enqueue is not None:
		my_enqueue.clear()
