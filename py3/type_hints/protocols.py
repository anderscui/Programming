# coding=utf-8
from typing import Protocol


class Quackable(Protocol):
    def quack(self) -> None:
        ...  # this is just a method signature


class Duck:
    def quack(self):
        print('Quack!')


class Dog:
    def bark(self):
        print('Woof!')


def run_quack(obj: Quackable):
    obj.quack()


if __name__ == '__main__':
    run_quack(Duck())
    # AttributeError: 'Dog' object has no attribute 'quack'
    run_quack(Dog())  # Expected type 'Quackable', got 'Dog' instead
