# Enter your code here. Read input from STDIN. Print output to STDOUT
ans = True
a = set(map(int, input().split()))
for i in range(int(input())):
    s = set(map(int, input().split()))
    if s != a and a.issuperset(s) and ans == True:
        ans = True
    else:
        ans = False
print(ans)
