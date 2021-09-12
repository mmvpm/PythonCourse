import random
from typing import final


SUIT_NAMES = ('♧', '♢', '♡', '♤')

RANK_NAMES = (
    '2', '3', '4', '5', '6', '7', '8', '9', '10',
    'Jack', 'Queen', 'King', 'Ace'
)


@final
class Card(object):
    """Represents a standard playing card."""

    def __init__(self, rank, suit):
        if suit not in SUIT_NAMES:
            raise ValueError('Unknown suit')
        if rank not in RANK_NAMES:
            raise ValueError('Unknown rank')
        
        self.rank = rank
        self.suit = suit
        self.value = RANK_NAMES.index(rank)

    def __str__(self):
        return f'{self.rank} {self.suit}'
    
    def __repr__(self):
        return str(self)

    def __eq__(self, other):
        return self.value == other.value

    def __lt__(self, other):
        return self.value < other.value


@final
class Deck(object):
    """Represents a deck of cards."""

    def __init__(self):
        self._cards = [
            Card(rank, suit) \
                for suit in SUIT_NAMES \
                    for rank in RANK_NAMES
        ]

    def __str__(self):
        return str(self._cards)
    
    def __repr__(self):
        return str(self)

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


class AbstractCombination():
    """Represents a combination in poker."""

    def __init__(self, cards):
        self._cards = cards

    def __eq__(self, other):
        return sorted(self._cards) == sorted(other._cards)

    def __repr__(self):
        return f'{type(self).__name__}({self._cards})'

    def high_card(self):
        # rule: Ace = 1 if all other cards have rank < 9 
        special_case = max(self._cards[1:]).value < RANK_NAMES.index('9')
        if self._cards[0].rank == 'Ace' and special_case:
            return self._cards[1]
        return self._cards[0]

    @classmethod
    def from_cards(cls, cards):
        if len(cards) != 5:
            raise ValueError('len(cards) should be 5')
        cards = sorted(cards, reverse=True)
        cards = cls._find_cards(cards)
        if cards is not None:
            return cls(cards)
        return None

    @classmethod
    def _find_cards(cls, cards):
        raise NotImplementedError('This method')


@final
class HighCard(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        return cards


@final
class Pair(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        for i in range(len(cards) - 1):
            if cards[i] == cards[i + 1]:
                return (cards[i], cards[i + 1])


@final
class DoublePair(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        result = []
        for i in range(len(cards) - 1):
            if cards[i] == cards[i + 1]:
                result.append(cards[i])
                result.append(cards[i + 1])
                i += 1
        if len(result) >= 4:
            return result[:4]


@final
class Triplet(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        for i in range(len(cards) - 2):
            if cards[i] == cards[i + 1] == cards[i + 2]:
                return (cards[i], cards[i + 1], cards[i + 2])


@final
class Straight(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        # rule: [A, 5, 4, 3, 2] -> [5, 4, 3, 2, A]
        special_case = max(cards[1:]).value < RANK_NAMES.index('6')
        if cards[0].rank == 'Ace' and special_case:
            cards[0].value = -1 # minimum
            cards = sorted(cards, reverse=True)

        for i in range(len(cards) - 1):
            if cards[i].value != cards[i + 1].value + 1:
                return None
        return cards


@final
class Flush(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        suits = list(map(lambda card: card.suit, cards))
        if suits.count(suits[0]) == len(suits):
            return cards


@final
class FullHouse(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        [a, b, c, d, e] = cards # cards list is sorted
        # => 2 options for full hause: [2, 2, 3, 3, 3] or [3, 3, 3, 2, 2]
        if (a == b == c and d == e) or (a == b and c == d == e):
            return cards


@final
class Quads(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        [a, b, c, d, e] = cards
        if a == b == c == d:
            return (a, b, c, d)
        if b == c == d == e:
            return (b, c, d, e)


@final
class StraightFlush(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        flush = Flush.from_cards(cards)
        straight = Straight.from_cards(cards)
        if flush is not None and straight is not None:
            return cards


@final
class RoyalFlush(AbstractCombination):
    @classmethod
    def _find_cards(cls, cards):
        straight_flush = StraightFlush.from_cards(cards)
        if straight_flush is not None and cards[0].rank == 'Ace':
            return cards


# Combinations in descending order
COMBINATIONS = (
    RoyalFlush,
    StraightFlush,
    Quads,
    FullHouse,
    Flush,
    Straight,
    Triplet,
    DoublePair,
    Pair,
    HighCard
)


def compare_combinations(a, b):
    """Returns 1 if a > b, 2 if b > a, otherwise 0"""
    a_index = COMBINATIONS.index(type(a))
    b_index = COMBINATIONS.index(type(b))
    if a_index < b_index: # a > b
        return 1
    if a_index > b_index: # b > a
        return 2
    # now a_index == b_index
    if a.high_card() > b.high_card(): # a > b
        return 1
    if a.high_card() < b.high_card(): # b > a
        return 2
    return 0


@final
class Hand(object):
    """Represents a hand of playing cards."""

    def __init__(self):
        self._cards = []
    
    def __repr__(self):
        return str(self._cards)

    def add_card(self, card):
        """Add a card to the deck."""
        self._cards.append(card)

    def top_combination(self):
        for combination_type in COMBINATIONS:
            combination = combination_type.from_cards(self._cards)
            if combination is not None:
                return combination
        return None  # No combinations found


def get_winner(player1, player2):
    """Returns 1 if player1 wins, otherwise 2."""
    top_comb1 = player1.top_combination()
    top_comb2 = player2.top_combination()
    return compare_combinations(top_comb1, top_comb2)


if __name__ == '__main__':
    deck = Deck()
    deck.shuffle()

    player1 = Hand()
    player2 = Hand()

    deck.move_cards(player1, 5)
    deck.move_cards(player2, 5)

    print(f'Player 1: {player1} -> {player1.top_combination()}')
    print(f'Player 2: {player2} -> {player2.top_combination()}')

    result = get_winner(player1, player2)
    print('Draw' if result == 0 else f'Player {result} wins')
