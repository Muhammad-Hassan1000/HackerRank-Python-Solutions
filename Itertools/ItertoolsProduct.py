from itertools import product
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
b.sort()
print(*product(a, b))
