# Enter your code here. Read input from STDIN. Print output to STDOUT
from collections import OrderedDict
dword = set()
wlist = OrderedDict()
for i in range(int(input())):
    word = input()
    dword.add(word)
    if word not in wlist:
        wlist[word] = "1"
    else:
        wlist[word] = str(int(wlist[word]) + 1)
print(len(dword))
for x in wlist.values():
    print(x, end=" ")
