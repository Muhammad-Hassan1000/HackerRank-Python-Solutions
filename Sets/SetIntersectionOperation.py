# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
er = set(input().split())
french = int(input())
fr = set(input().split())
common = er.intersection(fr)
print(len(common))
