from typing import Sequence, TypeVar
import random
_Tt = TypeVar("T")


def sort(container: Sequence[_Tt]) -> Sequence[_Tt]:
	"""
	Sort input container with quick sort

	:param container: container of elements to be sorted
	:return: container sorted in ascending order
	"""

	def quick(container):
		left = []
		mid = []
		right = []
		lst = []
		if len(container) > 1:
			m = container[random.randint(container(min()), container(max())]
			for x in container:
				if x < m:
					left.append(x)
				elif x == m:
					mid.append(x)
				elif x > m:
					right.append(x)
			# return sort(left) + mid + sort(right)
		lst.extend(sort(left))
		lst.extend(mid)
		lst.extend(sort(right))
		return lst
	container = quick(container)
	return container
