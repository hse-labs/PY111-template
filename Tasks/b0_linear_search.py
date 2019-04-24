"""
This module implements some functions based on linear search algo
"""

import numpy as np
arr = np.array([1, 2, 3, 4, -5, 6, 7])


def min_search(arr) -> int:
	"""
	Function that find minimal element in array

	:param arr: Array containing numbers
	:return: index of first occurrence of minimal element in array
	"""
	arr_min = arr[0]
	index = 0
	index_min = 0
	for i in range(len(arr)):
		index += 1
		if arr[i] < arr_min:
			arr_min = arr[i]
			index_min = int(index) - 1
	print(arr_min, index_min)
	return -1


min_search(arr)
