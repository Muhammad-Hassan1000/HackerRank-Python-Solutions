def average(array):
    s = set(array)
    l = len(s)
    avg = round(sum(s) / l, 3)
    return avg

