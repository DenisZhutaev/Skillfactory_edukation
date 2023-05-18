import pytest


def unique_id(val):
    return "{}".format(val)


@pytest.mark.parametrize('param', (
        [-1, -2, -3],
        [0, 0, 0],
        [1, 4, 5],
        [2, 2, 2]), ids=unique_id)

def test_triangle(param):
    if 0 != sum(param) > 3 and (sum(param) % 3) == 0:
        assert True
    else:
        assert False
