def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""
	n1, n2 = 0, len(arr) - 1
	mid = (n1 // 2 + n2 // 2) + 1
	approx = 1
	while elem != arr[mid] and n2 - n1 > approx:
		mid = int(n1 / 2 + n2 / 2)
		if elem > arr[mid]:
			n1 = mid
		elif elem < arr[mid]:
			n2 = mid
		else:
			return mid
	if elem == arr[n1] or elem == arr[n2]:
		return n1 if elem == n1 else n2
	return None


if __name__ == '__main__':
	print(binary_search(1, [1, 2, 3, 4, 5, 6, 7, 8, 9]))
