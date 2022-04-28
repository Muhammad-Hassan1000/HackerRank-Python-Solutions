import re
for _ in range(int(input())):
    isValid = True
    try:
        regex = re.compile(input())
    except re.error:
        isValid = False
    print(isValid)
