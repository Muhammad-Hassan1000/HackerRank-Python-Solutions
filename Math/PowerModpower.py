# Enter your code here. Read input from STDIN. Print output to STDOUT
from math import pow
a = float(input())
b = float(input())
m = float(input())
print(int(a**b))
print(int(pow(a,b) % m))
