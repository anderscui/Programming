# coding=utf-8
class LineItem:
    def __init__(self, description, weight, price):
        self.description = description
        # here the property setter is used.
        self.weight = weight
        self.price = price

    @property
    def weight(self):
        return self._weight

    @weight.setter
    def weight(self, value):
        print('write value to property')
        if value > 0:
            self._weight = value
        else:
            raise ValueError(f'value must be > 0')

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(raisins.subtotal())

    raisins.weight = -20
    print(raisins.subtotal())
