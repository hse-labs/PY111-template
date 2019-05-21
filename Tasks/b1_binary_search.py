def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	x = 0
	y = len(arr) - 1
	answer = None
	while x <= y:
		q = (x + y) // 2
		if arr[q] == elem:
			answer = q
			break
		elif arr[q] > elem:
			y = q - 1
		elif arr[q] < elem:
			x = q + 1
	return answer
