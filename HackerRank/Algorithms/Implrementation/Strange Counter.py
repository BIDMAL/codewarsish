inp = '10000000'
inp = '17'
t = int(inp)

def StrangeCounter(t):
    sc = 3
    k = 1
    while (t-sc) > 0:
        t -= sc
        k *= 2
        sc = 3*k
    return(sc-t+1) 

print(StrangeCounter(t))