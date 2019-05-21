"""
Priority Queue
Queue priorities are from 0 to 5
"""

priority_queue = {i: [] for i in range(6)}


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue
	:param elem: element to be added
	:return: Nothing
	"""
	global priorrity_queue
	print(priority_queue[priority])
	priority_queue[priority].append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue
	:return: dequeued element
	"""
	global priority_queue
	for i in range(6):
		if priority_queue[i]:
			return priority_queue[i].pop(0)


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it
	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global priority_queue
	return priority_queue[priority][ind]


def clear() -> None:
	"""
	Clear my queue
	:return: None
	"""
	global priority_queue
	for key in priority_queue:
		priority_queue[key].clear()
	return None
