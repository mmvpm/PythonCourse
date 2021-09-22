from contract import *


def test_arg_types_happy_path():
    
    @contract(arg_types=(int, float))
    def add_two_numbers(first, second):
        return first + second
    
    add_two_numbers(1, 2.0)


def test_arg_types_failed():
    
    @contract(arg_types=(int, float))
    def add_two_numbers(first, second):
        return first + second
    
    try:
        add_two_numbers(1, 2) # (int, int)
    except ContractError:
        pass # ok
    except Exception:
        assert False


def test_arg_types_any():
    
    @contract(arg_types=(int, Any))
    def add_two_numbers(first, second):
        return first + second
    
    add_two_numbers(1, 2.0)


def test_arg_types_wrong_any():
    
    @contract(arg_types=(Any, float))
    def add_two_numbers(first, second):
        return first + second
    
    try:
        add_two_numbers(1, 2) # (int, int)
    except ContractError:
        pass # ok
    except Exception:
        assert False


def test_arg_types_none():
    
    @contract(arg_types=None)
    def add_two_numbers(first, second):
        return first + second
    
    add_two_numbers(1, 2.0)