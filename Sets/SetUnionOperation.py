# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
er = input().split()
french = int(input())
fr = input().split()
er = set(er)
fr = set(fr)
total = er.union(fr)
print(len(total))
