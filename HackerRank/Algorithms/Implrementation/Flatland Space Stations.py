inp = ['99992 4',
       '90467 18058 99109 48463']

n, m = map(int, inp[0].split())
sps = sorted(list(map(int, inp[1].split())))

dist = 0
if n != m:
    stpt = 0
    endpt = sps[0]
    dist = max(dist, endpt-stpt)
    stpt = endpt
    for i in range(1, len(sps)):
        endpt = sps[i]
        dist = max(dist, (endpt-stpt)//2)
        stpt = endpt
    endpt = n-1
    dist = max(dist, endpt-stpt)
print(dist)