# Enter your code here. Read input from STDIN. Print output to STDOUT
eng = int(input())
er = set(input().split())
french = int(input())
fr = set(input().split())
onlyeng = er.difference(fr)
print(len(onlyeng))
