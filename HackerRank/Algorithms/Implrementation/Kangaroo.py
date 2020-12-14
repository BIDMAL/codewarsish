inp = '0 2 5 3'

def kangaroo(x1, v1, x2, v2):
    pos = x2 - x1
    if pos != 0:
        res = 'NO'
    else:
        res = 'YES'
    meet = (x2-x1)*(v2-v1) < 0
    while ((x2 - x1)*pos > 0) and meet:
        x1 += v1
        x2 += v2
        if x1 == x2:
            res = 'YES'
    return(res)

x1, v1, x2, v2 = map(int, inp.split())
print(kangaroo(x1, v1, x2, v2))