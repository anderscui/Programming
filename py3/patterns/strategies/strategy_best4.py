# coding=utf-8
# strategy_best4.py
# Strategy pattern -- function-based implementation
# selecting best promotion from list of functions
# registered by a decorator
from decimal import Decimal
from typing import Callable

from strategy import Order

Promotion = Callable[[Order], Decimal]

promos: list[Promotion] = []  # <1>


def promotion(promo: Promotion) -> Promotion:  # <2>
    promos.append(promo)
    return promo


def best_promo(order: Order) -> Decimal:
    """Compute the best discount available"""
    return max(promo(order) for promo in promos)  # <3>


@promotion  # <4>
def fidelity(order: Order) -> Decimal:
    """5% discount for customers with 1000 or more fidelity points"""
    if order.customer.fidelity >= 1000:
        return order.total() * Decimal('0.05')
    return Decimal(0)


@promotion
def bulk_item(order: Order) -> Decimal:
    """10% discount for each LineItem with 20 or more units"""
    discount = Decimal(0)
    for item in order.cart:
        if item.quantity >= 20:
            discount += item.total() * Decimal('0.1')
    return discount


@promotion
def large_order(order: Order) -> Decimal:
    """7% discount for orders with 10 or more distinct items"""
    distinct_items = {item.product for item in order.cart}
    if len(distinct_items) >= 10:
        return order.total() * Decimal('0.07')
    return Decimal(0)
