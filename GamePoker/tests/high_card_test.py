import sys
sys.path.append('C:\\Users\\Xiaomi\\Desktop\\Projects\\Python\\PythonCourse\\GamePoker')

from poker import HighCard
from test_data import *


def test_high_card():
    cards = [card6c, cardAc, cardKc, card8c, card7c]
    assert HighCard.from_cards(cards).high_card() == cardAc


def test_happy_path():
    cards = [cardAc, cardKc, card8c, card7c, card6c]
    assert HighCard.from_cards(cards) == HighCard(cards)
