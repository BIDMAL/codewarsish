inp = '0 0 1 0 0 1 0'
inp2 = '0 0 0 1 0 0'
ar = list(map(int, inp.split()))
ar2 = list(map(int, inp2.split()))

def jumpingOnClouds(c):
    cnt = 0
    ind = 0
    c.append(0)
    while ind < (len(c) - 2):
        ind += 1 + (not (c[ind+2]))
        cnt += 1
    return(cnt)

print(jumpingOnClouds(ar))
print(jumpingOnClouds(ar2))