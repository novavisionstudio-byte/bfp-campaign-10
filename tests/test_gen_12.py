from app.gen_12 import value_12


def test_value_12():
    assert value_12(2) == 2 * 7 + 7
    assert value_12(0) == 7
