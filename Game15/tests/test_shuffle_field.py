
from homework3.game import shuffle_field


def test_length():
    result = shuffle_field()
    assert len(result) == 16


def test_randomness():
    result1 = shuffle_field()
    result2 = shuffle_field()
    assert result1 != result2


def test_type():
    result = shuffle_field()
    assert isinstance(result, list)
