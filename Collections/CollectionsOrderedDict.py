# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
stock = OrderedDict()
for i in range(int(input())):
    item = input().split()
    name = " ".join(item[:-1])
    price = item[-1]
    if name in stock.keys():
        stock[name] = str(int(stock[name]) + int(price))
    else:
        stock[name] = str(int(price))
for x, y in stock.items():
    print(x, int(y))
