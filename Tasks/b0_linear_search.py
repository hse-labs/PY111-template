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
	for i in range(len(arr)):
		if arr[i] < arr[index]:
			index = i
	return index
