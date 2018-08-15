from .array_binary_search import array_binary_search
import pytest


def test_even_input():
    """test a list with an even number of elements
    """
    expected = 1
    result = array_binary_search([1, 2, 3, 4], 2)
    assert expected == result

def test_even_input_beginning():
    """ test a list with an even number of elements, correct index at the beginning
    """
    expected = 0
    result = array_binary_search([1, 2, 3, 4, 5], 1)
    assert expected == result


def test_even_input_end():
    """ test a list with an even number of elements, correct index at the end
    """
    expected = 3
    result = array_binary_search([1, 2, 3, 4], 4)
    assert expected == result


def test_even_input_not_found():
    """ test a list with an even number of elements
    """
    expected = -1
    result = array_binary_search([1, 2, 3, 4], 0)
    assert expected == result


def test_odd_input():
    """ test a list with an odd number of elements
    """
    expected = 1
    result = array_binary_search([1, 2, 3, 4, 5], 2)
    assert expected == result


def test_odd_input_beginning():
    """ test a list with an odd number of elements
    """
    expected = 0
    result = array_binary_search([1, 2, 3, 4, 5], 1)
    assert expected == result


def test_odd_input_end():
    """ test a list with an odd number of elements
    """
    expected = 4
    result = array_binary_search([1, 2, 3, 4, 5], 5)
    assert expected == result


def test_empty_input():
    """ test a list with no elements
    """
    expected = -1
    result = array_binary_search([], 0)
    assert expected == result


def test_element_gets_indexed_wrong():
    with pytest.raises(Exception):
        array_binary_search({[0,1,3]}, 'goop')
