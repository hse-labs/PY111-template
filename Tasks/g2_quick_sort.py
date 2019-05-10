# from typing import Sequence, TypeVar

# T = TypeVar("T")


def sort(container: list) -> list:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <= 1:
		return container
	compare = container[0]
	left = []
	middle = []
	right = []
	for i in container:
		if i < compare:
			left.append(i)
		elif i == compare:
			middle.append(i)
		else:
			right.append(i)
	return sort(left) + middle + sort(right)
