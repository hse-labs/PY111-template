def binary_search(elem, arr, low=0, high=None):
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:param low: minimum index
	:param high: maximum index
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	if high is None:
		high = len(arr) - 1
	if high < low:
		return None

	mid = (low + high) // 2

	if arr[mid] == elem:
		return mid
	elif elem > arr[mid]:
		return binary_search(elem, arr, mid + 1, high)
	elif elem < arr[mid]:
		return binary_search(elem, arr, low, mid-1)