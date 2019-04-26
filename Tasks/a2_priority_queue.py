"""
Priority Queue

Queue priorities are from 0 to 5
"""
q = [[], [], [], [], [], []]


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""

	global q
	qq = q[priority]
	qq.insert(0, elem)
	del q[priority]
	q.insert(priority, qq)
	return None


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	global q
	if q[5] != []:
		qq = q[5]
		del q[5]
		del qq[-1]
		q.insert(5, qq)
	elif q[4] != []:
		qq = q[4]
		del q[4]
		del qq[-1]
		q.insert(4, qq)
	elif q[3] != []:
		qq = q[3]
		del q[3]
		del qq[-1]
		q.insert(3, qq)
	elif q[2] != []:
		qq = q[2]
		del q[2]
		del qq[-1]
		q.insert(2, qq)
	elif q[1] != []:
		qq = q[1]
		del q[1]
		del qq[-1]
		q.insert(1, qq)
	elif q[0] != []:
		qq = q[0]
		del q[0]
		del qq[-1]
		q.insert(0, qq)
	return qq[-1]


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	global q
	qq = q[priority]
	return qq[ind]


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	global q
	q = [[], [], [], [], [], []]
	return None


if __name__ == "__main__":
	enqueue(0, 0)
	enqueue(11, 1)
	enqueue(22, 2)
	enqueue(22, 2)
	print(q)
	print(len(q[2]))
	print(peek(0, 1))
	print(dequeue())
	print(q)
	clear()
	print(q)
