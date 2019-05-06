"""
This module implements some functions based on linear search algo
"""

arr = []


def min_search(arr) -> int:
	"""
	Function that find minimal element in array
	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""

	minimum_element = arr[0]
	minimum_index = 0

	for index, element in enumerate(arr):
		if element <= minimum_element:
			minimum_element = element
			minimum_index = index

	return minimum_index
