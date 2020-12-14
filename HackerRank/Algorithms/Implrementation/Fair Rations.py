inp = '2 3 4 5 6'
#inp = '1 2'
B = list(map(int, inp.split()))

def fairRations(B):
    odd = 0
    pos = []
    ind = 0
    for p in B:
        if p%2 != 0:
            odd += 1
            pos.append(ind)
        ind += 1
    if odd%2 != 0:
        return('NO')
    else:
        ops = 0
        for i in range(len(pos)//2):
            ops += pos[2*i+1]-pos[2*i]
        return(ops*2)

print(fairRations(B))