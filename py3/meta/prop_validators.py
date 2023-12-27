# coding=utf-8
from abc import ABC, abstractmethod


class Validated(ABC):
    def __set_name__(self, owner, name):
        self.storage_name = name

    def __set__(self, instance, value):
        print(f'setting value of prop {self.storage_name}')
        value = self.validate(self.storage_name, value)
        instance.__dict__[self.storage_name] = value

    @abstractmethod
    def validate(self, name, value):
        """return validated value or raise ValueError"""


class Quantity(Validated):
    """A quantity should be greater than 0."""

    def validate(self, name, value):
        if value <= 0:
            raise ValueError(f'`{name}` must be > 0.')
        return value


class NonBlank(Validated):
    """A string with at least one non-space char."""

    def validate(self, name, value: str):
        value = value.strip()
        if not value:
            raise ValueError(f'`{name}` cannot be blank.')
        return value
