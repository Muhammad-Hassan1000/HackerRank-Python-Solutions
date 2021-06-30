# Enter your code here. Read input from STDIN. Print output to STDOUT
nA = int(input())
a = set(map(int, input().split()))
for i in range(int(input())):
    op, length = map(str, input().split())
    s = set(map(int, input().split()))
    ans = eval("a.{0}({1})".format(op, s))
print(sum(a))
