#inp = ['8 2',
#       '0 0 1 0 0 1 1 0']

inp = ['10 3',
       '1 1 1 0 1 1 0 0 0 0']

n, k = map(int, inp[0].split())
clds = list(map(int, inp[1].split()))

def jumpingOnClouds(c, k):
    ensp = 1 + 2 * (c[0] == 1)    
    n = len(c)
    i = k
    while i%n != 0:
        ensp += 1 + 2 * (c[i%n] == 1)
        i += k
    return(100 - ensp)

print(jumpingOnClouds(clds, k))