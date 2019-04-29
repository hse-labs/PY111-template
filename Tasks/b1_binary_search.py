def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	low = 0
	high = len(arr)

	while low <= high:
		mid = (low + high) // 2
		if elem < arr[mid]:
			high = mid - 1
		elif elem > arr[mid]:
			low = mid + 1
		else:
			return mid
