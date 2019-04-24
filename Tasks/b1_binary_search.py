def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	m = 0
	n = len(arr)
	if elem < arr[0]:
		return None
	while elem != arr[int((m + n) // 2)]:
		if m + 1 == n:
			return None
		elif arr[int((m + n) // 2)] > elem:
			n = int((m + n) // 2)
		elif arr[int((m + n) // 2)] < elem:
			m = int((m + n) // 2)
		elif elem == arr[int((m + n) // 2)]:
			return (m + n) // 2
	return (m + n) // 2


if __name__ == "__main__":
	b = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
	print(binary_search(13, b))
