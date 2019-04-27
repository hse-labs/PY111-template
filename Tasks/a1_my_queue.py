"""
My little Queue
"""
from typing import Any


def enqueue(elem: Any) -> None:
	"""
	Operation that add element to the end of the queue

	:param elem: element to be added
	:return: Nothing
	"""
	print(elem)
	return None


def dequeue() -> Any:
	"""
	Return element from the beginning of the queue

	:return: dequeued element
	"""
	return None


def peek(ind: int = 0) -> Any:
	"""
	Allow you to see at the element in the queue without dequeuing it

	:param ind: index of element (count from the beginning)
	:return: peeked element
	"""
	print(ind)
	return None


def clear() -> None:
	"""
	Clear my queue

	:return: None
	"""
	return None
