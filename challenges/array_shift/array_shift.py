def insert_shift_array(input_array, input_item):
    """inserts given item at the middle of an even-length array, or to the right of the middle element in an odd-length array
    """

    # creates space in the array for shifting
    input_array += [0]
    # creates a stopping point for the while loop
    mid = len(input_array) // 2

    i = len(input_array) - 1
    while i > mid:
        input_array[i] = input_array[i-1]
        i -= 1

    input_array[mid] = input_item
    return input_array


"""
    empty list

    int
    iterable
    nothing
    none

    fail < expect error
    a b d type error
    c inputs expected

    if type(arr) is not list:
        raise TyperError('Gnarf - there was an error')
"""
