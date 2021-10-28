import pytest
import random

from contract import Any
from contract import contract
from contract import ContractError


def test_arg_types_happy_path(add_two_numbers):
    contract(arg_types=(int, float))(add_two_numbers)(1, 2.0)


def test_arg_types_failed(add_two_numbers):
    with pytest.raises(ContractError):
        contract(arg_types=(int, float))(add_two_numbers)(1, 2)


def test_arg_types_any(add_two_numbers):
    contract(arg_types=(int, Any))(add_two_numbers)(1, 2.0)


def test_arg_types_wrong_any(add_two_numbers):
    with pytest.raises(ContractError):
        contract(arg_types=(Any, float))(add_two_numbers)(1, 2)


def test_arg_types_none(add_two_numbers):
    contract(arg_types=None)(add_two_numbers)(1, 2.0)


@pytest.mark.timeout(10)
def test_arg_types_random_numbers(add_two_numbers):
    first_number = random.randint(0, 5)
    second_number = random.random()
    contract(arg_types=(int, float))(add_two_numbers)(first_number, second_number)


@pytest.mark.parametrize(
    'first_number',
    [1, 2, 3, 5, 8, 13]
)
@pytest.mark.parametrize(
    'second_number',
    [0, 1, 2, 3, 5, 8]
)
def test_arg_types_special_numbers(add_two_numbers, first_number, second_number):
    contract(arg_types=(int, int))(add_two_numbers)(first_number, second_number)
