from .multi_bracket_validation import multi_bracket_validation
import pytest


# __init__
def test_basic_true():
    assert multi_bracket_validation('()') is True
