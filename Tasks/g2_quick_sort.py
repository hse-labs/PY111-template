from typing import Collection, TypeVar
from random import choice

_Tt = TypeVar("_Tt")




def sort(container: Collection[_Tt]) -> Collection[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	container = list(container)
	if len(container) <= 1:
		return container
	ref_el = choice(container)
	right_list = [i for i in container if i > ref_el]
	r = sort(right_list)
	left_list = [i for i in container if i < ref_el]
	l = sort(left_list)
	c = [i for i in container if i == ref_el]

	result = l + c + r
	return result

