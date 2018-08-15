from .array_shift import insert_shift_array
import pytest
# def test_access_test_folder():
#     pass

def test_even_input():
    """test a list with an even number of elements
    """
    expected = [1, 3, 2]
    result = insert_shift_array([1, 2], 3)
    assert expected == result

def test_odd_input():
    """ test a list with an odd number of elements
    """
    expected = [1, 2, 3, 1]
    result = insert_shift_array([1, 2, 1], 3)
    assert expected == result


def test_empty_input():
    """ test a list with no elements
    """
    expected = [3]
    result = insert_shift_array([], 3)
    assert expected == result

def test_arguement_must_be_valid_list():
    """ test an input of the incorrect type
    """
    with pytest.raises(TypeError):
      insert_shift_array({}, '')
