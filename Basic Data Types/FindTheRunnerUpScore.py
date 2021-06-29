if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    high = max(arr)
    num = len(arr)
    i = 0
    while i < num:
        if arr[i] == high:
            arr.remove(arr[i])
            num -= 1
            i -= 1
        i += 1
    arr.sort()
    print(arr[-1])        
