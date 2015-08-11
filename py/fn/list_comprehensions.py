nums = [1, 2, 3, 4, 5]
squares = [n * n for n in nums]
print(squares)

import math

vectors = [(1, 2), (3, 4), (5, 6)]
dist = [math.sqrt(x * x + y * y) for x, y in vectors]
print(dist)

# conditions
a = [-1, 3, 0, 5, 9]
print([i for i in a if i > 0])