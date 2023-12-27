# coding=utf-8


class Quantity:
    def __set_name__(self, owner, name):
        # this is that __init__ does
        self.storage_name = name

    # def __get__(self, instance, owner):
    #     """owner: a reference to the managed class (LineItem)"""
    #     # print(f'instance: {instance}')
    #     # print(f'owner: {owner}')
    #     return instance.__dict__[self.storage_name]

    def __set__(self, instance, value):
        """self: descriptor instance (a Quantity instance, e.g. LineItem.weight)
           instance: managed instance (a LineItem instance)
           value:
        """
        print(f'setting value for prop {self.storage_name}')
        if value > 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError(f'{self.storage_name} must be > 0')


class LineItem:
    weight = Quantity()
    price = Quantity()

    def __init__(self, description, weight, price):
        self.description = description
        # here the property setter is used.
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


if __name__ == '__main__':
    raisins = LineItem('Golden raisins', 10, 6.95)
    print(raisins.subtotal())
    print(raisins.__dict__)

    raisins.weight = -20
    print(raisins.subtotal())
