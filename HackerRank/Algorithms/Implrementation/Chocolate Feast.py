inp = '12 4 4'
n, c, m = map(int, inp.split())


def chocolateFeast(n, c, m):
    counter = 0
    buy = n // c
    counter += buy
    while buy >= m:
        wraps = buy // m
        counter += wraps
        buy = buy % m + wraps
    return(counter)

print(chocolateFeast(n, c, m))