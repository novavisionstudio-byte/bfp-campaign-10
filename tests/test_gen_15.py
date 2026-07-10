from app.gen_15 import value_15


def test_value_15():
    assert value_15(2) == 2 * 9 + 1
    assert value_15(0) == 1
