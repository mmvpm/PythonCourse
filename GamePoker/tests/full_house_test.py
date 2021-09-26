from poker import FullHouse
from test_data import *


def test_happy_path():
    cards = [card6c, card6h, card6d, card7c, card7h]
    assert FullHouse.from_cards(cards) == FullHouse(cards)


def test_happy_path_shuffled():
    cards = [card6c, card7h, card6h, card6d, card7c]
    assert FullHouse.from_cards(cards) == FullHouse(cards)


def test_no_full_house():
    cards = [card6c, card10s, card7h, card8d, cardAh]
    assert FullHouse.from_cards(cards) == None