from typing import Sequence, TypeVar

_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	def merge(left, right):
		lst = []
		while left and right:
			if left[0] < right[0]:
				lst.append(left.pop(0))
			else:
				lst.append(right.pop(0))
		if left:
			lst.extend(left)
		if right:
			lst.extend(right)
		return lst

	length = len(container)
	if length >= 2:
		mid = round(int(length / 2))
		container = merge(sort(container[:mid]), sort(container[mid:]))

	return container
