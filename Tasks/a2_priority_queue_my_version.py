"""
Priority Queue

Queue priorities are from 0 to 5
"""
my_priority_enqueue = []


def enqueue(elem, priority: int = 0) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:param priority: element priority
	:return: Nothing
	"""
	global my_priority_enqueue
	item = [elem, priority]
	ind = 0
	for counter, value in enumerate(my_priority_enqueue):
		if item[1] == value[1]:
			ind = counter + 1
		elif item[1] > value[1]:
			ind = counter + 1
	my_priority_enqueue = my_priority_enqueue[:ind] + [item] + my_priority_enqueue[ind:]


def dequeue():
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	if my_priority_enqueue:
		return my_priority_enqueue.pop(0)


def peek(ind: int = 0, priority: int = 0):
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:param priority: element priority
	:return: peeked element
	"""
	global my_priority_enqueue
	local_counter = 0
	for counter, value in enumerate(my_priority_enqueue):
		if priority == value[1]:
			if local_counter == ind:
				return my_priority_enqueue[counter]
			local_counter += 1


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	if my_priority_enqueue is not None:
		my_priority_enqueue.clear()
	return None

print(my_priority_enqueue)
clear()
print(my_priority_enqueue)
enqueue('new_elem')
print(my_priority_enqueue)
enqueue('new_elem2', 1)
print(my_priority_enqueue)
enqueue('new_elem2', 4)
print(my_priority_enqueue)
print(dequeue())
print(my_priority_enqueue)
print(peek(0, 1))
print(peek(1, 1))
print(peek(0, 3))
