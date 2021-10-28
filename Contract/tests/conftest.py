import os
import sys
import pytest

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)


@pytest.fixture(scope='session')
def add_two_numbers():
    return lambda first, second: first + int(second)
