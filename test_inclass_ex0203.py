import pytest


def test_find_gradient(coordinate1, coordinate2):
    from inclass_ex0203 import create_equation
    coordinate1 = [1, 1]
    coordinate2 = [2, 2]
    answer = create_equation(coordinate1, coordinate2)
    # Assert
    assert answer == 1