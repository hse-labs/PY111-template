def binary_search(elem, arr):
    """
    Performs binary search of given element inside of array (using recursive way)

    :param elem: element to be found
    :param arr: array where element is to be found
    :return: Index of element if it's presented in the arr, None otherwise
    """
    idx = len(arr) // 2
    if elem < arr[0] or elem > arr[-1]:  # or just check if elem not in arr
        return None
    elif elem == arr[idx]:
        return idx
    elif elem > arr[idx]:
        try:
            idx += binary_search(elem, arr[idx:])
        except TypeError:
            return None
        else:
            return idx
    elif elem < arr[idx]:
        idx = binary_search(elem, arr[: idx])
        return idx
    else:
        return ValueError


if __name__ == '__main__':
    print(binary_search(-1, [i for i in range(1, 6)]))
