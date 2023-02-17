import pytest


@pytest.mark.parametrize("coordinate1, coordinate2, expected",
                         [((1, 1), (2, 2), 1),
                          ((3, 2), (11, 6), 0.5),
                          ])
def test_find_gradient(coordinate1, coordinate2, expected):
    from inclass_ex0203 import find_gradient
    answer = find_gradient(coordinate1, coordinate2)
    # Assert
    assert answer == expected


@pytest.mark.parametrize("m, coordinate1, expected",
                         [(1, (1, 1), 0),
                          (3, (2, 7), 1),
                          ])
def test_find_y_intercept(m, coordinate1, expected):
    from inclass_ex0203 import find_y_intercept
    answer = find_y_intercept(m, coordinate1)
    # Assert
    assert answer == expected


@pytest.mark.parametrize("x, m, c, expected",
                         [(1, 2, 1, 3),
                          (3, 2, 7, 13),
                          ])
def test_find_y(x, m, c, expected):
    from inclass_ex0203 import find_y
    answer = find_y(x, m, c)
    # Assert
    assert answer == expected
