from poker import StraightFlush
from test_data import *


def test_happy_path():
    cards = [card6c, card7c, card8c, card9c, card10c]
    assert StraightFlush.from_cards(cards) == StraightFlush(cards)


def test_happy_path_shuffled():
    cards = [card7c, card8c, card6c, card10c, card9c]
    assert StraightFlush.from_cards(cards) == StraightFlush(cards)


def test_only_straight():
    cards = [card7c, card8c, card6h, card10c, card9c]
    assert StraightFlush.from_cards(cards) == None


def test_only_flush():
    cards = [card7c, card8c, cardAc, card10c, card9c]
    assert StraightFlush.from_cards(cards) == None


def test_last_ace():
    cards = [card10c, cardJc, cardQc, cardKc, cardAc]
    assert StraightFlush.from_cards(cards) == StraightFlush(cards)


def test_first_ace():
    cards = [cardAc, card2c, card3c, card4c, card5c]
    assert StraightFlush.from_cards(cards) == StraightFlush(cards)
