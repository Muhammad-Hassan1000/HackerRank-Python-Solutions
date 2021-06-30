# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
er = set(input().split())
french = int(input())
fr = set(input().split())
one = er.symmetric_difference(fr)
print(len(one))
