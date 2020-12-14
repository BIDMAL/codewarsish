import collections
n, m = [5, 3]
A = list('aabab')
B = list('abc')
d = collections.defaultdict(list)
for i in range(m):
    pos = 1
    if B[i] not in A[pos-1:]:
        d[B[i]].append(-1)
    while B[i] in A[pos-1:]:
        ind = A[pos-1:].index(B[i])
        d[B[i]].append(pos+ind)
        pos += ind+1

vals = list(d.values())
for i in range (len(vals)):
    print(*vals[i])

