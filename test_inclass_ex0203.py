import pytest

@pytest.mark.parametrize("coordinate1, coordinate2, expected",
                         [([1, 1], [2, 2], 1),
                          ([3, 2], [11, 6], 0.5),
                          ])
def test_find_gradient(coordinate1, coordinate2, expected):
    from inclass_ex0203 import find_gradient
    answer = find_gradient(coordinate1, coordinate2)
    # Assert
    assert answer == expected
    
    
