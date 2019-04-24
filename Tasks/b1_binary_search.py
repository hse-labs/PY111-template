import numpy as np
arr = np.array([])
elem = int


def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	i = 0
	j = len(arr) - 1
	m = int(j / 2)
	while arr[m] != elem and i < j:
		if elem > arr[m]:
			i = m + 1
		else:
			j = m - 1
		m = int((i + j) / 2)
	if i > j:
		return None
	else:
		return m

