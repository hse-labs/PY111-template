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
	for i in arr:
		if i < min_num:
			min_num = i
	return arr.index(min_num)
