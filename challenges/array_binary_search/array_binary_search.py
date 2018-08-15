def array_binary_search(given_array, search_key):
    """finds the index of a given search key within a given sorted list, and return its index. Otherwise, return -1.
    """
    low = 0
    high = len(given_array) - 1
    mid = len(given_array) // 2
    while low != high and low < high:
        if given_array[mid] > search_key:
            high = mid
        elif given_array[mid] < search_key:
            low = mid
        elif given_array[mid] == search_key:
            return mid
        mid = get_mid(low, high)

    if(given_array[mid] == search_key):
        return mid
    else:
        return -1


def get_mid(low, high):
    """returns the int occurring at the midpoint of the ints low and high
    """
    return low + high // 2
