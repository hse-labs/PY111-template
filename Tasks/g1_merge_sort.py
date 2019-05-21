from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	x = len(container)
	if x <= 1:
		return container
	left = sort(container[:x // 2])
	right = sort(container[x//2: x])

	i = 0
	j = 0
	y = []

	while i < len(left) or j < len(right):
		if not i < len(left):
			y.append(right[j])
			j += 1
		elif not j < len(right):
			y.append(left[i])
			i += 1
		elif left[i] < right[j]:
			y.append(left[i])
			i += 1
		else:
			y.append(right[j])
			j += 1
	return y
