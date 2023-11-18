# coding=utf-8
from collections import namedtuple, abc

Card = namedtuple('Card', ('rank', 'suit'))


class FrenchDeck(abc.MutableSequence):
    ranks = [str(n) for n in range(2, 11)] + list('JQKA')
    suits = 'spade diamond club heart'

    def __init__(self):
        self._cards = [Card(rank, suit) for suit in self.suits
                       for rank in self.ranks]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, index):
        return self._cards[index]

    def __setitem__(self, index, value):
        self._cards[index] = value

    def __delitem__(self, index):
        del self._cards[index]

    def insert(self, index, value):
        self._cards.insert(index, value)
