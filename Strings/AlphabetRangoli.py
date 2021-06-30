def print_rangoli(size):
    import string
    width = 4 * size - 3
    alpha = string.ascii_lowercase
    l = []
    for i in range(n):
        s = "-".join(alpha[i:n])
        l.append(s[::-1]+s[1:])

    for i in range(n-1, 0, -1):
        print(l[i].center(width, "-"))

    for i in range(n):
        print(l[i].center(width, "-"))



