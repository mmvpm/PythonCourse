from contract import *


def test_raises_happy_path():

    @contract(raises=(ValueError,))
    def add_two_numbers(first, second):
        return first + int(second)

    add_two_numbers(1, 2.0)


def test_raises_right_error():

    @contract(raises=(ValueError,))
    def add_two_numbers(first, second):
        return first + int(second)

    try:
        add_two_numbers(1, 'a')
    except ValueError:
        pass  # ok
    except Exception:
        assert False


def test_raises_wrong_error():

    @contract(raises=(TypeError,))
    def add_two_numbers(first, second):
        return first + int(second)

    try:
        add_two_numbers(1, 'a')
    except ContractError:
        pass  # ok
    except Exception:
        assert False


def test_raises_none():

    @contract(raises=None)
    def add_two_numbers(first, second):
        return first + int(second)

    try:
        add_two_numbers(1, 'a')
    except ValueError:
        pass  # ok
    except Exception:
        assert False
