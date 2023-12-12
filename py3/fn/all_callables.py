# coding=utf-8
import random


class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)

    def pick(self):
        try:
            return self._items.pop()
        except IndexError:
            raise LookupError(f'pick from emtpy {type(self).__name__}')

    def __call__(self, *args, **kwargs):
        return self.pick()


if __name__ == '__main__':
    bingo = BingoCage(range(3))
    assert callable(bingo)
    print(bingo.pick(), bingo())
