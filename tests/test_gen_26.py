from app.gen_26 import value_26


def test_value_26():
    assert value_26(2) == 2 * 4 + 3
    assert value_26(0) == 3
