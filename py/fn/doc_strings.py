def factorial(n):
    """Computes n factorial. e.g.:

    >>> factorial(5)
    120
    >>>
    """
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

print(factorial.__doc__)