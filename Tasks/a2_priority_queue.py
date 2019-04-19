"""
Priority Queue

Queue priorities are from 0 to 5
"""
priority_queue = []

def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global priority_queue
	priority_queue.append((priority, elem))
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global priority_queue
	if priority_queue[0]:
		priority_queue.sort(key=lambda x: x[0])
		elem = priority_queue[0][1]
		del (priority_queue[0])
		return elem
	else:
		return None


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global priority_queue
	if priority_queue[ind]:
		priority_queue.sort(key=lambda x: x[0])
		elem = priority_queue[0][1]
		del (priority_queue[0])
		return elem
	else:
		return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global priority_queue
	priority_queue = []
	return None
