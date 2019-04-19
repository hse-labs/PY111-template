"""
My little Stack
"""
elems = []

def push(elem) -> None:
	"""
	Operation that add element to stack

	:param elem: element to be pushed
	:return: Nothing
	"""
	global elems
	#elems.insert(0, elem)
	elems.append(elem)

	return None


def pop():
	"""
	Pop element from the top of the stack

	:return: popped element
	"""
	global elems
	if elems == []:
		return None
	else:
		pop_elem = elems[-1]
		del elems[-1]
		return pop_elem


def peek(ind=0):
	"""
	Allow you to see at the element in the stack without popping it

	:param ind: index of element (count from the top)
	:return: peeked element
	"""
	global elems
	if ind > len(elems)-1:
		return None
	else:
		# peeked_elem = elems[ind]
		# return peeked_elem
		return elems[ind-1]

def clear() -> None:
	"""
	Clear my stack

	:return: None
	"""
	global elems
	elems = []

	return None

if __name__ == '__main__':
	push(43)
	push(41)
	push(2)
	push(5)
	push(8)
	print(elems)
	print(pop())
	print(elems)
	print(peek(1))
	print(elems)
	clear()
	print(elems)
