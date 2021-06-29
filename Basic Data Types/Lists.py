if __name__ == '__main__':
    N = int(input())
    l = []
    for i in range(N):
        a = input().split()
        cmd = a[0]
        arg = a[1:]
        if cmd != "print":
            cmd = cmd + "("+ ",".join(arg) +")"
            eval("l." + cmd)
        else:
            print(l)    
