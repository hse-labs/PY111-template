"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	index = 0
	m = arr[index]
	for i in range(0, len(arr)):
		if arr[i] < m:
			m = arr[i]
			index = i
	return index
