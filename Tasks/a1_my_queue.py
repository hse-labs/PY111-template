"""
My little Queue
"""
priority_queue = []


def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue
	:param elem: element to be added
	:return: Nothing
	"""
	global priority_queue
	queue.append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue
	:return: dequeued element
	"""
	global priority_queue
	if len(queue) == 0:
		return None
	else:
		dequeued_element = queue[0]
		del queue[0]
		return dequeued_element


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it
	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global priority_queue
	if ind > len(queue) - 1:
		return None
	else:
		return queue[ind]


def clear() -> None:
	"""
	Clear my queue
	:return: None
	"""
	global priority_queue
	queue = []
	return None
