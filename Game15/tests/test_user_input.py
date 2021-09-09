
import contextlib

import game
from game import handle_user_input


@contextlib.contextmanager
def _patch_user_input(obj, value):
    """
    This helper function is used to mock user input,
    since I didn't want to install a mocking library just
    for this task.
    """
    obj.get_char = lambda: value.encode()

    yield

    # setting values back just in case:
    obj.input = input


def test_right_input():
    with _patch_user_input(game, 'w'):
        move = handle_user_input()
    assert move == 'w'
