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
	return queue.pop(0) if queue else None


def peek(ind: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global queue
	return queue[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global queue
	queue.clear()
	return None


if __name__ == '__main__':
	for i in range(10):
		enqueue(i)
		print(queue)
		print(dequeue())
	print(queue)