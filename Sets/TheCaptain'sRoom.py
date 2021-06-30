# Enter your code here. Read input from STDIN. Print output to STDOUT
k = int(input())
tourists = list(map(int, input().split()))
rooms = set(tourists)
print(((sum(rooms)*k) - (sum(tourists)))//(k-1))
