from typing import Collection, TypeVar

_Tt = TypeVar("_Tt")


def merge(left, right):
	result = []
	while left and right:
		if left[0] <= right[0]:
			result.append(left[0])
			del left[0]
		elif left[0] > right[0]:
			result.append(right[0])
			del right[0]
	result += left + right
	return result


def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	container = list(container)
	if len(container) <= 1:
		return container
	middle = len(container)//2
	right_list = container[middle: len(container)]
	r = sort(right_list)
	left_list = container[0: middle]
	l = sort(left_list)

	result = merge(l, r)
	return result

