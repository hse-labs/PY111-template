from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	container = list(container)
	changes = True
	counter = 1
	while changes:
		changes = False
		for i in range(len(container)-counter):
			if container[i] > container[i+1]:
				container[i], container[i+1] = container[i+1], container[i]
				changes = True
		counter += 1
	return container
