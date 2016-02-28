from collections import defaultdict


word_freqs = [('a', 10), ('b', 20), ('a', 5), ('c', 25)]
d = defaultdict(int)
for w, f in word_freqs:
    d[w] += f

print(d)
assert len(d) == 3
assert d['a'] == 15
assert d['b'] == 20
assert d['c'] == 25
assert d['d'] == 0
