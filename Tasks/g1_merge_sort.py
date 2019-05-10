from typing import Sequence, TypeVar

T = TypeVar("T")


def sort(container: Sequence[T]) -> Sequence[T]:
	"""
	Sort input container with merge sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""
	if len(container) <= 1:
		return container
	mid = len(container) // 2
	left = sort(container[:mid])
	right = sort(container[mid:])
	return merge(left, right)


def merge(r_list: Sequence[T], l_list: Sequence[T]) -> Sequence[T]:
	"""
	Merging of left and right slices of the 'container'

	:param l_list: 'left' from 'sort' function
	:param r_list: 'right' from 'sort' function
	:return: merged list
	"""
	sum_list = []
	i = j = 0
	while i < len(l_list) and j < len(r_list):
		if l_list[i] <= r_list[j]:
			sum_list.append(l_list[i])
			i += 1
		else:
			sum_list.append(r_list[j])
			j += 1
	sum_list += l_list[i:]
	sum_list += r_list[j:]
	return sum_list
