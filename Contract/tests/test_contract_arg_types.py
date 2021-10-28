import pytest
import random
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
        pytest.fail()


def test_arg_types_none():
    
    @contract(arg_types=None)
    def add_two_numbers(first, second):
        return first + second
    
    add_two_numbers(1, 2.0)


@pytest.mark.timeout(10)
def test_arg_types_random_numbers():
    
    @contract(arg_types=(int, float))
    def add_two_numbers(first, second):
        return first + second
    
    first_number = random.randint(0, 5)
    second_number = random.random()
    add_two_numbers(first_number, second_number)


@pytest.mark.parametrize(
    'first_number', 
    [1, 2, 3, 5, 8, 13]
)
@pytest.mark.parametrize(
    'second_number', 
    [0, 1, 2, 3, 5, 8]
)
def test_arg_types_special_numbers(first_number, second_number):
    
    @contract(arg_types=(int, int))
    def add_two_numbers(first, second):
        return first + second

    add_two_numbers(first_number, second_number)


def test_arg_types_dataset(dataset):
    
    @contract(arg_types=(float, float))
    def add_two_numbers(first, second):
        return first + second

    for test_case in dataset:
        add_two_numbers(*test_case)
