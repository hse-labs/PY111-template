from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""
	Sort input container with bubble sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	n = len(container)

	for i in range(n - 1):
		for j in range(n - i - 1):
			if container[j] > container[j + 1]:
				buff, container[j] = container[j], container[j + 1]
				container[j + 1] = buff

	return container
