m1 = int(input())
m = set(map(int, input().split()))
n1 = int(input())
n = set(map(int, input().split()))
a = m.symmetric_difference(n)
s = list(a)
s.sort()
for i in s:
    print(i)

