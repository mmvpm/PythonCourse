import pytest

from contract import contract
from contract import ContractError


def test_raises_happy_path(add_two_numbers):
    contract(raises=(ValueError,))(add_two_numbers)(1, 2.0)


def test_raises_right_error(add_two_numbers):
    with pytest.raises(ValueError):
        contract(raises=(ValueError,))(add_two_numbers)(1, 'a')


def test_raises_wrong_error(add_two_numbers):
    with pytest.raises(ContractError):
        contract(raises=(TypeError,))(add_two_numbers)(1, 'a')


def test_raises_none(add_two_numbers):
    with pytest.raises(ValueError):
        contract(raises=None)(add_two_numbers)(1, 'a')
