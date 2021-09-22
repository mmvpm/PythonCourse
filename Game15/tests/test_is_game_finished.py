from game import EMPTY_MARK, FIELD_SIZE, is_game_finished


def test_finished_state():
    finished_state = list(range(1, FIELD_SIZE ** 2))
    finished_state.append(EMPTY_MARK)

    result = is_game_finished(finished_state)
    assert result is True


def test_unfinished_states():
    unfinished_state = list(range(1, FIELD_SIZE ** 2))
    unfinished_state.append(EMPTY_MARK)
    unfinished_state[0], unfinished_state[-1] = \
        unfinished_state[-1], unfinished_state[0]

    result = is_game_finished(unfinished_state)
    assert result is False
