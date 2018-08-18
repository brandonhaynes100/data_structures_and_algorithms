from linked_list import LinkedList, Node, Any
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
