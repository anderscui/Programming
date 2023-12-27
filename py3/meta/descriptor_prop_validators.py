# coding=utf-8
from meta.prop_validators import Quantity, NonBlank


class LineItem:
    description = NonBlank()
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(raisins.subtotal())
    print(raisins.__dict__)

    raisins.description = ' \t '
    print(raisins.subtotal())
