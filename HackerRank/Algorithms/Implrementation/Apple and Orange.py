inp = ['7 11',
       '5 15',
       '3 2',
       '-2 2 1',
       '5 -6']

def countApplesAndOranges(s, t, a, b, apples, oranges):
    npa = [a + x for x in apples]
    npb = [b + x for x in oranges]
    res = [0, 0]
    for x in npa:
        res[0] += (x >= s) and (x <= t)
    for x in npb:
        res[1] += (x >= s) and (x <= t)
    print(*res, sep='\n')

st = inp[0].split()
s = int(st[0])
t = int(st[1])
ab = inp[1].split()
a = int(ab[0])
b = int(ab[1])
mn = inp[2].split()
m = int(mn[0])
n = int(mn[1])
apples = list(map(int, inp[3].rstrip().split()))
oranges = list(map(int, inp[4].rstrip().split()))
countApplesAndOranges(s, t, a, b, apples, oranges)