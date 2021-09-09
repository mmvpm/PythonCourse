
import pytest

from homework3.game import EMPTY_MARK, perform_move

left_down_corner_index = 12
right_up_corner_index = 3


@pytest.fixture(scope='function')
def left_down_corner():
    def inner():
        state = list(range(1, 16))
        state[0], state[1] = state[1], state[0]
        state.insert(left_down_corner_index, EMPTY_MARK)

        return state
    return inner


@pytest.fixture(scope='function')
def right_up_corner(left_down_corner):
    def inner():
        state = left_down_corner()
        state[left_down_corner_index], state[right_up_corner_index] = \
            state[right_up_corner_index], state[left_down_corner_index]

        return state
    return inner


# Actual tests:

def test_up_move(left_down_corner):
    state = left_down_corner()
    result = perform_move(state, 'w')

    result_index = result.index(EMPTY_MARK)
    assert result_index == left_down_corner_index - 4


def test_right_move(left_down_corner):
    state = left_down_corner()
    result = perform_move(state, 'd')

    result_index = result.index(EMPTY_MARK)
    assert result_index == left_down_corner_index + 1


def test_left_move(right_up_corner):
    state = right_up_corner()
    result = perform_move(state, 'a')

    result_index = result.index(EMPTY_MARK)
    assert result_index == right_up_corner_index - 1


def test_down_move(right_up_corner):
    state = right_up_corner()
    result = perform_move(state, 's')

    result_index = result.index(EMPTY_MARK)
    assert result_index == right_up_corner_index + 4


def test_bad_moves(left_down_corner, right_up_corner):
    state = right_up_corner()
    assert perform_move(state, 'w') is None
    assert perform_move(state, 'd') is None

    state = left_down_corner()
    assert perform_move(state, 'a') is None
    assert perform_move(state, 's') is None
