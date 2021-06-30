def swap_case(s):
    a = ""
    for i in range(len(s)):
        if ord(s[i]) >= 65 and ord(s[i]) <= 90:
            b = s[i].lower()
        elif ord(s[i]) >= 97 and ord(s[i]) <= 122:
            b = s[i].upper()
        else:
            b = s[i]
        a = a + b
    return a

