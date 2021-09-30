"""15 puzzle implementation."""


from msvcrt import getch as get_char
from os import system
from random import shuffle
from time import sleep
from types import MappingProxyType

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Exit from the game
EXIT_EVENT = 'exit'

# Field has a size of (FIELD_SIZE x FIELD_SIZE)
FIELD_SIZE = 4

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = MappingProxyType({
    'w': -FIELD_SIZE,
    's': FIELD_SIZE,
    'a': -1,
    'd': 1,
})


def _sign(permutation):
    inverses = sum(
        first_value > second_value
        for index, first_value in enumerate(permutation)
        for _, second_value in enumerate(permutation[index + 1:])
    )
    return 1 if inverses % 2 == 0 else -1


def shuffle_field():
    """Create a field at the very start of the game.

    Returns:
        list with FIELD_SIZE ** 2 randomly shuffled tiles,
        one of which is a empty space.
    """
    field = list(range(1, FIELD_SIZE ** 2))
    shuffle(field)

    if _sign(field) == -1:  # impossible to solve
        # swap two first tiles to make it possible
        field[1], field[0] = field[0], field[1]

    field.append(EMPTY_MARK)
    return field


def print_field(field):
    """Print field to user.

    Args:
        field: current field state to be printed.
    """
    system('cls')  # clear screen from the old field
    print('Управление на клавиши WASD (Ctrl+C для выхода)')
    for index, tile in enumerate(field):
        print(tile, end=' ')
        if index % FIELD_SIZE == FIELD_SIZE - 1:
            print()


def is_game_finished(field):
    """Check if the game is finished.

    Args:
        field: current field state.

    Returns:
        True if the game is finished, False otherwise.
    """
    initial_field = list(range(1, FIELD_SIZE ** 2))
    initial_field.append(EMPTY_MARK)
    return field == initial_field


def perform_move(field, key):
    """Move empty-tile inside the field.

    Args:
        field: current field state.
        key: move direction.

    Returns:
        new field state (after the move)
        or `None` if the move can't me done.
    """
    def _validate_move(index):
        return 0 <= index < len(field) \
            and not (key == 'd' and index % FIELD_SIZE == 0) \
            and not (key == 'a' and index % FIELD_SIZE == FIELD_SIZE - 1)

    current_index = field.index(EMPTY_MARK)
    target_index = current_index + MOVES[key]
    if _validate_move(target_index):
        field[current_index], field[target_index] = \
            field[target_index], field[current_index]
        return field


def handle_user_input():
    """Handle user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    Returns:
        <str> current move.
    """
    try:
        # waits for only one symbol from keyboard
        move = get_char().decode('utf-8')
    except Exception:
        return None

    if move in MOVES.keys():
        return move
    elif move == '\x03':  # Ctrl+C
        return EXIT_EVENT


def main():
    """Run game."""
    field = shuffle_field()
    print_field(field)

    moves_counter = 0
    while not is_game_finished(field):
        key = handle_user_input()
        if key == EXIT_EVENT:
            break
        elif key is None:
            continue

        if perform_move(field, key) is not None:
            moves_counter += 1
        else:
            print('Некорректный ход')
            sleep(0.5)

        print_field(field)

    if is_game_finished(field):
        print('Победа! Сделано ходов: {0}'.format(moves_counter))


if __name__ == '__main__':
    main()
