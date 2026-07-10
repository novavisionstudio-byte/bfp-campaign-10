from app.gen_2 import value_2


def test_value_2():
    assert value_2(2) == 2 * 9 + 4
    assert value_2(0) == 4
