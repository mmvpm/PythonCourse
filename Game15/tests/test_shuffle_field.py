from game import FIELD_SIZE, shuffle_field


def test_length():
    result = shuffle_field()
    assert len(result) == FIELD_SIZE ** 2


def test_randomness():
    result1 = shuffle_field()
    result2 = shuffle_field()
    assert result1 != result2


def test_type():
    result = shuffle_field()
    assert isinstance(result, list)
