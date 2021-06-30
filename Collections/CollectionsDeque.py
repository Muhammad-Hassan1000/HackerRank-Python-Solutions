# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import deque
d = deque()
for i in range(int(input())):
    op, *val = input().split()
    getattr(d,op)(*val)
print(*d)
