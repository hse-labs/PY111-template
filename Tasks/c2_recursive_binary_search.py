def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array (using recursive way)

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	ind = len(arr)//2
	if arr[ind] == elem:
		return ind
	elif len(arr) == 1 and arr[ind] != elem:
		return None
	else:
		if arr[ind] > elem:
			ind = binary_search(elem, arr[:ind])
			return ind
		elif arr[ind] < elem:
			try:
				ind = ind + binary_search(elem, arr[ind:])
			except TypeError:
				return None
			return ind
