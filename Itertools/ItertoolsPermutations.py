# Enter your code here. Read input from STDIN. Print output to STDOUT
from itertools import permutations
s, k = map(str, input().split())
k = int(k)
a = list()
per = list(permutations(s, k))
for i in range(len(per)):
    a.append("".join(per[i]))
    a.sort()
for i in a:
    print(i)
