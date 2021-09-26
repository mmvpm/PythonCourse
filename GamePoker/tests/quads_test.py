from poker import Quads
from test_data import *


def test_happy_path():
    cards = [card6c, card6h, card6d, card6s, card7h]
    assert Quads.from_cards(cards) == Quads([card6c, card6h, card6d, card6s])


def test_happy_path_shuffled():
    cards = [card6c, card7c, card6h, card6d, card6s]
    assert Quads.from_cards(cards) == Quads([card6c, card6h, card6d, card6s])


def test_one_triplet():
    cards = [card6c, card7c, cardAh, card6d, card6s]
    assert Quads.from_cards(cards) == None