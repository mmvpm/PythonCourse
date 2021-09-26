from poker import RoyalFlush
from test_data import *


def test_happy_path():
    cards = [card10c, cardJc, cardQc, cardKc, cardAc]
    assert RoyalFlush.from_cards(cards) == RoyalFlush(cards)


def test_happy_path_shuffled():
    cards = [cardAc, cardJc, cardKc, cardQc, card10c]
    assert RoyalFlush.from_cards(cards) == RoyalFlush(cards)


def test_only_straight_flush():
    cards = [card7c, card8c, card6c, card10c, card9c]
    assert RoyalFlush.from_cards(cards) == None
