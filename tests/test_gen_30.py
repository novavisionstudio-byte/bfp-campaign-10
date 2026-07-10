from app.gen_30 import value_30


def test_value_30():
    assert value_30(2) == 2 * 9 + 5
    assert value_30(0) == 5
