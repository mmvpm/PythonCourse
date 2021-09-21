from msvcrt import getch as get_char
from os import system
from random import shuffle
from time import sleep

# Empty tile, there's only one empty cell on a field:
EMPTY_MARK = 'x'

# Exit from the game
EXIT_EVENT = 'exit'

# Field has a size of (FIELD_SIZE x FIELD_SIZE) 
FIELD_SIZE = 4

# Dictionary of possible moves if a form of:
# key -> delta to move the empty tile on a field.
MOVES = {
    'w': -FIELD_SIZE,
    's': FIELD_SIZE,
    'a': -1,
    'd': 1,
}


def shuffle_field():
    """
    This function is used to create a field at the very start of the game.

    :return: list with FIELD_SIZE ** 2 randomly shuffled tiles,
        one of which is a empty space.
    """

    def sign(permutation):
        inverses = 0
        for i in range(len(permutation)):
            for j in range(i + 1, len(permutation)):
                inverses += permutation[i] > permutation[j]
        return 1 if inverses % 2 == 0 else -1

    field = list(range(1, FIELD_SIZE ** 2))
    shuffle(field)
    
    if sign(field) == -1: # impossible to solve
        field[0], field[1] = field[1], field[0] # now sign(field) == 1
    
    field.append(EMPTY_MARK)
    return field


def print_field(field):
    """
    This function prints field to user.

    :param field: current field state to be printed.
    :return: None
    """
    system('cls') # clear screen from the old field
    print('Управление на клавиши WASD (Ctrl+C для выхода)')
    for i in range(FIELD_SIZE):
        for j in range(FIELD_SIZE):
            print(f'{field[i * FIELD_SIZE + j]:>3}', end = '')
        print()


def is_game_finished(field):
    """
    This function checks if the game is finished.

    :param field: current field state.
    :return: True if the game is finished, False otherwise.
    """
    initial_field = list(range(1, FIELD_SIZE ** 2))
    initial_field.append(EMPTY_MARK)
    return field == initial_field


def perform_move(field, key):
    """
    Moves empty-tile inside the field.

    :param field: current field state.
    :param key: move direction.
    :return: new field state (after the move)
        or `None` if the move can't me done.
    """

    def validate_move(index):
        return 0 <= index < len(field) \
            and not (key == 'd' and index % FIELD_SIZE == 0) \
            and not (key == 'a' and index % FIELD_SIZE == FIELD_SIZE - 1)

    current_index = field.index(EMPTY_MARK)
    target_index = current_index + MOVES[key]
    if validate_move(target_index):
        field[current_index], field[target_index] = \
            field[target_index], field[current_index]
        return field
    else:
        return None


def handle_user_input():
    """
    Handles user input.

    List of accepted moves:
        'w' - up,
        's' - down,
        'a' - left,
        'd' - right

    :return: <str> current move.
    """
    try:
        # waits for only one symbol from keyboard
        move = get_char().decode('utf-8')
    except Exception as _:
        return None
    
    if move in MOVES.keys():
        return move
    elif move == '\x03': # Ctrl+C
        return EXIT_EVENT

def main():
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
        print(f'Победа! Сделано ходов: {moves_counter}')


if __name__ == '__main__':
    main()
