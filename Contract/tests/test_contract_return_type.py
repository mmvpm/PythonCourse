from contract import *


def test_return_type_happy_path():

    @contract(return_type=float)
    def add_two_numbers(first, second):
        return first + second

    add_two_numbers(1, 2.0)


def test_return_type_failed():

    @contract(return_type=float)
    def add_two_numbers(first, second):
        return first + second  # int

    try:
        add_two_numbers(1, 2)
    except ContractError:
        pass  # ok
    except Exception:
        assert False


def test_return_type_any():

    @contract(return_type=Any)
    def add_two_numbers(first, second):
        return first + second

    add_two_numbers(1, 2.0)


def test_return_type_none():

    @contract(return_type=None)
    def add_two_numbers(first, second):
        return first + second

    add_two_numbers(1, 2.0)
