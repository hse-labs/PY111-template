"""
My little Queue
"""
queue = []

def enqueue(elem) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	global queue
	queue.append(elem)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global queue
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
	global queue
	if ind > len(queue) - 1:
		return None
	else:
		return queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue = []
	return None


if __name__ == '__main__':
	enqueue(43)
	enqueue(45)
	enqueue(4)
	enqueue(3)
	print(queue)
	dequeue()
	print(queue)
	peek()
	print(queue)
	clear()
	print(queue)