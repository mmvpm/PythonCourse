import sys
sys.path.append('C:\\Users\\Xiaomi\\Desktop\\Projects\\Python\\PythonCourse\\GamePoker')

from poker import DoublePair
from test_data import *


def test_happy_path():
    cards = [card6h, card6c, card7h, card7c, cardAc]
    assert DoublePair.from_cards(cards) == DoublePair([card6h, card6c, card7h, card7c])


def test_happy_path_shuffled():
    cards = [card6h, cardAc, card6c, card7h, card7c]
    assert DoublePair.from_cards(cards) == DoublePair([card6h, card6c, card7h, card7c])


def test_no_pairs():
    cards = [card6h, cardKc, card7c, card8c, cardAc]
    assert DoublePair.from_cards(cards) == None


def test_one_pair():
    cards = [card6h, card6c, cardAc, card7h, card8c]
    assert DoublePair.from_cards(cards) == None


def test_all_equals():
    cards = [cardKc] * 5
    assert DoublePair.from_cards(cards) == DoublePair([cardKc] * 4)
