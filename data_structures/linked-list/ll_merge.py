from linked_list import LinkedList

# Write a function called mergeLists which takes two linked lists as arguments. Zip the two linked lists together into one so that the nodes alternate between the two lists and return a reference to the head of the zipped list. Try and keep additional space down to O(1). You have access to the Node class and all the properties on the Linked List class as well as the methods created in previous challenges.


def merge_lists(ll_one, ll_two):
    # if one of the lists is empty, return the other
    if not ll_one.head:
        return ll_two.head
    if not ll_two.head:
        return ll_one.head

    # while both lists still have values
    curr_one = ll_one.head
    curr_two = ll_two.head

    # for the case where ll_one runs out before ll_two
    prev_one = ll_one.head

    while curr_one and curr_two:
        # this line should preserve the last non-None node
        prev_one = curr_one

        temp_one = curr_one._next
        temp_two = curr_two._next

        curr_one._next = curr_two
        curr_two._next = temp_one

        curr_one = temp_one
        curr_two = temp_two

    # at this point, either curr_one or curr_two should be None
    if curr_one and not curr_two:
        # if there are still values left, skip to returning ll_one
        # because the remaing values are still in ll_one
        pass

    elif curr_two and not curr_one:
        # if there are still values left in ll_two, append them
        # to the end of ll_one
        prev_one._next = curr_two

    return ll_one.head
