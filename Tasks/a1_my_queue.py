"""
My little Queue
"""


my_queue = []


def enqueue(elem) -> None:
	"""

	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	my_queue.append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if my_queue == []:
		return None
	else:
		return my_queue.pop(0)


def peek(ind: int = 0):
	"""

	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return my_queue[ind]


def clear() -> None:
	"""

	Clear my queue

	:return: None
	"""
	my_queue.clear()
	return None
