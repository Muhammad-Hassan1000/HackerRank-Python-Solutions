# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import Counter
total = 0
x = input()
sizes = input()
n = int(input())
mylist = sizes.split()
record = dict(Counter(mylist).items())
for i in range(n):
    s, p = map(int, input().split())
    if str(s) in record.keys() and int(record[str(s)]) > 0:
        total += p
        record[str(s)] = str(int(record[str(s)]) - 1)
print(total)
