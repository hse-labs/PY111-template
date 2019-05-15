def binary_search(elem, arr):
    """
    Performs binary search of given element inside of array

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    left_bound = 0
    right_bound = len(arr)
    middle_ind = 1
    while right_bound-left_bound > 1:
        middle_ind = (left_bound+right_bound)//2
        if arr[middle_ind] > elem:
            right_bound = middle_ind
        elif arr[middle_ind] < elem:
            left_bound = middle_ind
        elif arr[middle_ind] == elem:
            return middle_ind
    if arr[middle_ind-1] == elem:
        return middle_ind-1
    return None
