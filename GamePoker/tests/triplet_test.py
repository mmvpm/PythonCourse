from poker import Triplet
from test_data import *


def test_happy_path():
    cards = [card6h, card6c, card6d, cardAc, card7c]
    assert Triplet.from_cards(cards) == Triplet([card6h, card6c, card6d])


def test_happy_path_shuffled():
    cards = [card6h, cardAc, card6d, card7c, card6c]
    assert Triplet.from_cards(cards) == Triplet([card6h, card6c, card6d])


def test_returns_none():
    cards = [card6h, cardKc, card7c, card8c, cardAc]
    assert Triplet.from_cards(cards) == None

def test_one_pair():
    cards = [card6h, card6c, cardAc, card7h, card8c]
    assert Triplet.from_cards(cards) == None


def test_all_equals():
    cards = [cardKc] * 5
    assert Triplet.from_cards(cards) == Triplet([cardKc] * 3)
