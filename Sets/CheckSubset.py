# Enter your code here. Read input from STDIN. Print output to STDOUT
T = int(input())
for i in range(T):
    nA = int(input())
    a = set(map(int, input().split()))
    nB = int(input())
    b = set(map(int, input().split()))
    print(a.issubset(b))
