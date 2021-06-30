# Enter your code here. Read input from STDIN. Print output to STDOUT
for i in range(int(input())):
    try:
        a, b = map(str, input().split())
        print(int(a) // int(b))
    except ZeroDivisionError as err:
        print("Error Code:", err)
    except ValueError as err:
        print("Error Code:", err)
