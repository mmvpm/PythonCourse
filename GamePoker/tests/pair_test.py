import sys
sys.path.append('C:\\Users\\Xiaomi\\Desktop\\Projects\\Python\\PythonCourse\\GamePoker')

from poker import Pair
from test_data import *


def test_happy_path():
    cards = [card6h, card6c, card7c, card8c, cardAc]
    assert Pair.from_cards(cards) == Pair([card6h, card6c])


def test_happy_path_shuffled():
    cards = [card7c, card6h, card8c, cardAc, card6c]
    assert Pair.from_cards(cards) == Pair([card6h, card6c])


def test_no_pairs():
    cards = [card6h, cardKc, card7c, card8c, cardAc]
    assert Pair.from_cards(cards) == None


def test_two_pairs():
    cards = [card6h, card6c, cardAc, card7h, card7c]
    assert Pair.from_cards(cards) == Pair([card7h, card7c])


def test_all_equals():
    cards = [cardKc] * 5
    assert Pair.from_cards(cards) == Pair([cardKc, cardKc])
