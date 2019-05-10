def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	lower_elem = 0
	mid_elem = len(arr) // 2
	upper_elem = len(arr) - 1
	while arr[mid_elem] != elem and lower_elem <= upper_elem:
		if elem > arr[mid_elem]:
			lower_elem = mid_elem + 1
		else:
			upper_elem = mid_elem - 1
		mid_elem = (lower_elem + upper_elem) // 2
	if lower_elem > upper_elem:
		return None
	else:
		return mid_elem
