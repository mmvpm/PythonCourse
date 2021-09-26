from poker import Straight
from test_data import *


def test_happy_path():
    cards = [card6c, card7h, card8d, card9s, card10s]
    assert Straight.from_cards(cards) == Straight(cards)


def test_happy_path_shuffled():
    cards = [card10s, card8d, card6c, card9s, card7h]
    assert Straight.from_cards(cards) == Straight(cards)


def test_no_straight():
    cards = [card6c, card10s, card7h, card8d, cardAh]
    assert Straight.from_cards(cards) == None


def test_last_ace():
    cards = [card10s, cardJc, cardQd, cardKs, cardAh]
    assert Straight.from_cards(cards) == Straight(cards)


def test_first_ace():
    cards = [cardAh, card2c, card3h, card4d, card5s]
    assert Straight.from_cards(cards) == Straight(cards)
