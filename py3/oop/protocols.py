# coding=utf-8
from collections.abc import Sized, Sequence
from collections import namedtuple
from typing import Sized as TSized

Card = namedtuple('Card', ('rank', 'suit'))


class Vowels:
    def __getitem__(self, i):
        return 'AEIOU'[i]

    def __len__(self):
        return 5


class FrenchDeck:
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spade diamond club heart'

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]


if __name__ == '__main__':
    v = Vowels()
    # iter, `in` op -> getitem
    print('A' in v, [c for c in v])

    print(isinstance(v, Sequence))
    print(isinstance(v, Sized))
    print(isinstance(v, TSized))

    Sequence.register(FrenchDeck)
    deck = FrenchDeck()
    print(isinstance(deck, Sequence))
