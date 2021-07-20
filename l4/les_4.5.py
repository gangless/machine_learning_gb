from functools import reduce
a = [i for i in range(100, 1001, 2)]
b = reduce(lambda x, y: x * y, a)
print(b)
