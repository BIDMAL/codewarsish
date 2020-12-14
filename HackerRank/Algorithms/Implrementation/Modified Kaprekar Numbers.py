p = 1
q = 20

def kaprekarNumbers(p, q):
    nms = []
    for i in range(p, q+1):        
        sq = i**2
        d = len(str(i)) 
        r = int(str(sq)[-d:])
        ld = len(str(sq))-d
        if ld:
            l = int(str(sq)[:ld])
        else:
            l = 0
        if l+r==i:
            nms.append(i)
    if len(nms):
        print(*nms)
    else:
        print('INVALID RANGE')

kaprekarNumbers(p, q)
