"""
Priority Queue

Queue priorities are from 0 to 5
"""
queue = {i: [] for i in range(6)}


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue[priority].append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global queue
	for i in queue:
		if queue[i]:
			deq_el = queue[i][0]
			del queue[i][0]
			return deq_el
	return None


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	if queue[priority]:
		return queue[priority][ind]
	return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue = {i: [] for i in range(6)}
	return None
