import pytest

from test2.calculations import add

@pytest.mark.parametrize("num1, num2, expected", [
    (3, 2, 5),
    (4, 5, 9),
    (12, 4, 16)
])
def test_add(num1, num2, expected):
    sum = add(num1, num2)
    assert sum == expected
 