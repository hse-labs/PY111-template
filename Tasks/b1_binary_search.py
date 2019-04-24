some_arr = [5,6,7,8,9,10]
some_elem = 9

def binary_search(elem, arr):
	"""
	Performs binary search of given element inside of array

	:param elem: element to be found
	:param arr: array where element is to be found
	:return: Index of element if it's presented in the arr, None otherwise
	"""

	founded = False
	current_index = len(arr)//2
	left_border = 0
	right_border = len(arr)
	true_index = None

	while not founded:
			if arr[current_index] > elem:
				right_border = current_index
			elif arr[current_index] < elem:
				left_border = current_index
			else:
				founded = True
				true_index = current_index
			current_index = (right_border + left_border) // 2
	return true_index


if __name__ == '__main__':
	print(binary_search(some_elem,some_arr))
