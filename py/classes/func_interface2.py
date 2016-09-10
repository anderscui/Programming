from collections import defaultdict


class BetterCountMissing(object):
    def __init__(self):
        self.added = 0

    def __call__(self):
        self.added += 1
        return 0


current = {'green': 12, 'blue': 3}
increments = [
    ('red', 5),
    ('blue', 17),
    ('orange', 9),
]

counter = BetterCountMissing()
result = defaultdict(counter, current)

for key, amount in increments:
    result[key] += amount

assert counter.added == 2
