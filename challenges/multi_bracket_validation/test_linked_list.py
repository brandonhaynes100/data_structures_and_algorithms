from linked_list import LinkedList
from ll_merge import merge_lists
import pytest


@pytest.fixture
def empty_list():
    return LinkedList()


@pytest.fixture
def small_list():
    ll = LinkedList()
    ll.insert(1)
    ll.insert(2)
    ll.insert(3)
    ll.insert(4)
    return ll
    # ll will be: [4, 3, 2, 1]


@pytest.fixture
def small_list_two():
    ll = LinkedList()
    ll.insert(5)
    ll.insert(6)
    ll.insert(7)
    ll.insert(8)
    return ll
    # ll will be: [8, 7, 6, 5]


# __init__
def test_linked_list_exists():
    assert LinkedList


def test_create_list_instance():
    ll = LinkedList()
    assert isinstance(ll, LinkedList)


def test_default_property_head(empty_list):
    assert empty_list.head is None


# __len__
def test_empty_list_length(empty_list):
    assert empty_list._len == 0


def test_small_list_length(small_list):
    assert small_list._len == 4


# __iter__
def test_iterator_exists(small_list):
    itr_node = small_list.__iter__()
    assert itr_node.val == small_list.head.val
    assert itr_node._next == small_list.head._next


def test_iterator_moves_independently(small_list):
    itr_node = small_list.__iter__()
    itr_node = itr_node._next
    assert itr_node.val != small_list.head.val


# insert
def test_insert_success(empty_list):
    assert empty_list.head is None
    empty_list.insert(25)
    assert empty_list.head.val == 25


def test_length_of_list_increases_on_insertion(empty_list):
    assert len(empty_list) == 0
    empty_list.insert(25)
    assert len(empty_list) == 1


# includes
def test_includes_returns_true_if_exists(small_list):
    assert small_list.includes(1) is True
    assert small_list.includes(4) is True


def test_includes_returns_false_if_not_exists(small_list):
    assert small_list.includes(100) is False
    assert small_list.includes(0) is False


# append
def test_append_present_empty_list(empty_list):
    empty_list.append(5)
    assert empty_list.includes(5)


# def test_append_present(small_list):
#     assert True


# def test_append_at_end(small_list):
#     assert True


# insert_before
def test_insert_before_empty_list(empty_list):
    empty_list.insert_before(5, 4)
    assert empty_list.includes(5)


# def test_insert_before_success(small_list):
#     assert True


# def test_insert_before_at_prior_index(small_list):
#     assert True


# insert_after
def test_insert_after_empty_list(empty_list):
    empty_list.insert_after(5, 4)
    assert empty_list.includes(5)


# def test_insert_after_present(small_list):
#     assert True


# def test_insert_after_at_following_index(small_list):
#     assert True

# kth_from_end
def test_kth_from_end(small_list):
    # small_list
    assert small_list.kth_from_end(0) == 1
    assert small_list.kth_from_end(1) == 2
    assert small_list.kth_from_end(2) == 3
    assert small_list.kth_from_end(3) == 4
    # empty_list
    # assert empty_list.kth_from_end(0) == None


# ll_merge
def test_ll_merge_basic_function(small_list, small_list_two):
    merged_lists = merge_lists(small_list, small_list_two)
    assert merged_lists.val == small_list.head.val


def test_ll_merge_ll_one_empty(empty_list, small_list):
    merged_lists = merge_lists(empty_list, small_list)
    assert merged_lists.val == small_list.head.val


def test_ll_merge_ll_two_empty(small_list, empty_list):
    merged_lists = merge_lists(small_list, empty_list)
    assert merged_lists.val == small_list.head.val
