inp = ['3 3',
       '2 5 6']

n, k = map(int, inp[0].split())
arr = list(map(int, inp[1].split()))

def getMinimumCost(k, c):
    c.sort(reverse=True)
    n = len(c)//k
    total = 0
    for i in range(n):
        total += (i+1)*sum(c[i*k:(i+1)*k])
    z = len(c)%k
    if z:
        total += (n+1)*sum(c[-z:])
    return total

print(getMinimumCost(k, arr))