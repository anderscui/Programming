# coding=utf-8
import abc
import random


class Tombola(abc.ABC):
    @abc.abstractmethod
    def load(self, iterable):
        """Add items from an iterable"""

    @abc.abstractmethod
    def pick(self):
        """
        Remove item at random, returning it.

        This method should raise `LookupError` when the instance is empty.
        """

    def loaded(self):
        """Return `True` if there's at least 1 item, `False` otherwise."""
        return bool(self.inspect())

    def inspect(self):
        """
        Return a sorted tuple with the items currently inside.
        """
        items = []
        while True:
            try:
                items.append(self.pick())
            except LookupError:
                break
        self.load(items)
        return tuple(items)


class BingoCage(Tombola):
    def __init__(self, items):
        self._randomizer = random.SystemRandom()
        self._items = []
        self.load(items)

    def load(self, iterable):
        self._items.extend(iterable)
        self._randomizer.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError(f'pick from emtpy {type(self).__name__}')

    def __call__(self):
        self.pick()


class LottoBlower(Tombola):
    def __init__(self, iterable):
        self._balls = list(iterable)

    def load(self, iterable):
        self._balls.extend(iterable)

    def pick(self):
        try:
            pos = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError(f'pick from emtpy {type(self).__name__}')
        return self._balls.pop(pos)

    def loaded(self):
        return bool(self._balls)

    def inspect(self):
        return tuple(self._balls)


class TomboList(list):
    def pick(self):
        if self:
            pos = random.randrange(len(self))
            return self.pop(pos)
        raise LookupError(f'pop from empty {type(self).__name__}')

    load = list.extend

    def loaded(self):
        return bool(self)

    def inspect(self):
        return tuple(self)


Tombola.register(TomboList)


if __name__ == '__main__':
    # tombola = Tombola()
    tombo_list = TomboList()
    print(issubclass(TomboList, Tombola), isinstance(tombo_list, Tombola))
