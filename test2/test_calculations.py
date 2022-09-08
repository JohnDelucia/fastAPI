from test2.calculations import add


def test_add():
    sum = add(5, 10)
    assert sum == 15
