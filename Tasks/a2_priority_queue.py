"""
Priority Queue

Queue priorities are from 0 to 5
"""

prior_queue = {i: [] for i in range(6)}


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global prior_queue
	print(prior_queue[priority])
	prior_queue[priority].append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global prior_queue
	for i in range(6):
		if prior_queue[i]:
			return prior_queue[i].pop(0)


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global prior_queue
	return prior_queue[priority][ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global prior_queue
	for key in prior_queue:
		prior_queue[key].clear()
	return None


if __name__ == '__main__':
	print(prior_queue)
	enqueue('vetka', 0)
	print(prior_queue)
	clear()
	print(prior_queue)