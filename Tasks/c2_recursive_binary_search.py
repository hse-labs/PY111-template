def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	mid = len(arr) // 2
	elem_pos = ((arr[0] + arr[-1]) // 2) + ((arr[0] + arr[-1]) % 2)
	if elem not in arr:
		return None
	if elem == arr[mid]:
		return elem_pos
	elif elem > arr[mid]:
		return binary_search(elem, arr[mid + 1:])
	else:
		return binary_search(elem, arr[:mid])
