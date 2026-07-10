from app.gen_19 import value_19


def test_value_19():
    assert value_19(2) == 2 * 7 + 6
    assert value_19(0) == 6
