"""
This module implements some functions based on linear search algo
"""


def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	min_num = arr[0]
	index_of_min_num = 0
	current_index = 0

	for i in arr:
		if i < min_num:
			min_num = i
			index_of_min_num = current_index
		current_index += 1
	return index_of_min_num
