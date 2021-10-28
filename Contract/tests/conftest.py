import os
import sys
import pytest

BASE_DIR = os.path.abspath(os.path.dirname(os.path.dirname(__file__)))
sys.path.append(BASE_DIR)


@pytest.fixture(scope='session')
def dataset():
    return [
        (1.2, 2.3),
        (3.4, 4.5),
        (5.6, 6.7),
    ]
