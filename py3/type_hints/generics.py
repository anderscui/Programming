# coding=utf-8
import random
from collections.abc import Iterable
from typing import Generic, TypeVar

from oop.custom_abcs import Tombola


T = TypeVar('T')


class LottoBlower(Tombola, Generic[T]):
    # here, declare the generic type T
    def __init__(self, items: Iterable):
        self._balls = list[T](items)

    def load(self, items: Iterable[T]):
        self._balls.extend(items)

    def pick(self) -> T:
        try:
            pos = random.randrange(len(self._balls))
        except ValueError:
            raise LookupError('pick from empty LottoBlower')
        return self._balls.pop(pos)

    def loaded(self) -> bool:
        return bool(self._balls)

    def inspect(self) -> tuple[T, ...]:
        return tuple(self._balls)


if __name__ == '__main__':
    lotto = LottoBlower[int]((1, 2, 3))
    # in pycharm, i is int
    i = lotto.pick()

