import sys
sys.path.append('C:\\Users\\Xiaomi\\Desktop\\Projects\\Python\\PythonCourse\\GamePoker')

from poker import Flush
from test_data import *


def test_happy_path():
    cards = [card6c, card7c, card8c, cardKc, cardAc]
    assert Flush.from_cards(cards) == Flush(cards)


def test_happy_path_shuffled():
    cards = [card8c, card6c, cardAc, card7c, cardKc]
    assert Flush.from_cards(cards) == Flush(cards)


def test_no_flush():
    cards = [card8c, card6c, cardAh, card7c, cardKc]
    assert Flush.from_cards(cards) == None
