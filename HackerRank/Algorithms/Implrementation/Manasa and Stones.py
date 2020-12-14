import itertools as it
n, a, b = [3, 1, 2]

def stones(n, a, b):
    res = set()
    outp = [a*(i!=0) for i in range(n)]
    res.add(sum(outp))
    for i in range(1,n):
        outp[i] = b
        res.add(sum(outp))
    return(sorted(res))

print(' '.join(map(str, stones(n, a, b))))
