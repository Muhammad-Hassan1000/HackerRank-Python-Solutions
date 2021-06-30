# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import *
N = int(input())
students = namedtuple('students', input().split())
student = [students(*input().split()) for i in range(N)]                 
avg = sum(float(i.MARKS) for i in student) / N
print("{:.2f}".format(avg))
