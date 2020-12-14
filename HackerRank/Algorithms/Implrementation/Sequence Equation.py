inp = '4 3 5 1 2'
sq = list(map(int, inp.split()))
def permutationEquation(p):
    res = []
    for i in range(1, len(p)+1):
        ind = p.index(i)+1
        res.append(p.index(p.index(i)+1)+1)
    return(res)
    #return([p.index(p.index(i)+1)+1 for i in range(1, len(p)+1)])

print(permutationEquation(sq))