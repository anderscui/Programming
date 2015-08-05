
import copy

a = [1, 2, [3, 4]]
b = copy.deepcopy(a)

b[2][0] = -100
print(b)
print(a)
