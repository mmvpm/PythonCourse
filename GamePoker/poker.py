import abc
import random
from typing import final


@final
class Card(object):
    """Represents a standard playing card."""

    def __init__(self, suit, suit_index, rank, rank_index):
        self.suit = suit
        self.suit_index = suit_index
        self.rank = rank
        self.rank_index = rank_index

    def __repr__(self):
        return '{0} of {1}'.format(self.rank, self.suit)

    def __lt__(self, other):
        if self.suit < other.suit:
            return True
        elif self.suit > other.suit:
            return False
        return self.rank < other.rank


@final
class Deck(object):
    """Represents a deck of cards."""

    SUIT_NAMES = ("Clubs", "Diamonds", "Hearts", "Spades")
    RANK_NAMES = (
        "Ace",
        "2", "3", "4", "5", "6", "7", "8", "9", "10",
        "Jack", "Queen", "King",
    )

    def __init__(self):
        self._cards = []
        for suit_index, suit in enumerate(self.SUIT_NAMES):
            for rand_index, rank in enumerate(self.RANK_NAMES):
                card = Card(
                    suit=suit,
                    suit_index=suit_index,
                    rank=rank,
                    rank_index=rand_index,
                )
                self._cards.append(card)

    def __str__(self):
        res = []
        for card in self._cards:
            res.append(str(card))
        return '\n'.join(res)

    def pop_card(self, index=-1):
        """
        Remove and return a card from the deck.
        By default, pop the last card.
        """
        return self._cards.pop(index)

    def shuffle(self):
        """Shuffle the cards in this deck."""
        random.shuffle(self._cards)

    def move_cards(self, hand, num):
        """Move the given number of cards from the deck into the Hand."""
        for _ in range(num):
            hand.add_card(self.pop_card())


class AbstractCombination(abc.ABCMeta):
    """Represents a combination in poker."""

    def __init__(self, cards):
        self._cards = cards

    @classmethod
    def from_cards(cls, cards):
        cards = cls._find_cards(cards)
        if cards is not None:
            return cls(cards)
        return None

    @classmethod
    def _find_cards(cls, cards):
        raise NotImplementedError('This method')


@final
class Pair(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        ...


@final
class Hand(object):
    """Represents a hand of playing cards."""

    COMBINATIONS = (
        Pair,
    )

    def __init__(self):
        self._cards = []

    def add_card(self, card):
        """Add a card to the deck."""
        self._cards.append(card)

    def top_combination(self):
        for combination_type in self.COMBINATIONS:
            combination = combination_type.from_cards(self._cards)
            if combination is not None:
                return combination
        return None  # No combinations found


def get_winner(player1, player2):
    """This function should print which player wins: first or second."""


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    player1 = Hand()
    player2 = Hand()

    deck.move_cards(player1, 5)
    deck.move_cards(player2, 5)
    print(get_winner(player1, player2))
