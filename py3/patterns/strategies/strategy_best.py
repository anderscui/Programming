# coding=utf-8
from decimal import Decimal

from strategy import Order
from strategy import fidelity_promo, bulk_item_promo, large_order_promo


# after adding a promo func, you should add it here too.
promos = [fidelity_promo, bulk_item_promo, large_order_promo]


def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)


if __name__ == '__main__':
    print(globals())
