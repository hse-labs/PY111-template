"""
Priority Queue

Queue priorities are from 0 to 5
"""


priority_queue = []


def enqueue(elem, priority) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:param priority: priority of the added element
	:return: Nothing
	"""
	if priority is None:
		priority_queue.append(elem)
	else:
		priority_queue.insert(priority, elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if not priority_queue:
		return None
	else:
		return priority_queue.pop(0)


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	return priority_queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	priority_queue.clear()
	return None
