import pytest

from contract import Any
from contract import contract
from contract import ContractError


def test_return_type_happy_path(add_two_numbers):
    contract(return_type=float)(add_two_numbers)(1.0, 2)


def test_return_type_failed(add_two_numbers):
    with pytest.raises(ContractError):
        contract(return_type=float)(add_two_numbers)(1, 2)


def test_return_type_any(add_two_numbers):
    contract(return_type=Any)(add_two_numbers)(1, 2.0)


def test_return_type_none(add_two_numbers):
    contract(return_type=None)(add_two_numbers)(1, 2.0)
