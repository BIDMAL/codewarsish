inp = ['6 3',
       '5 1',
       '2 1',
       '1 1',
       '8 1',
       '10 0',
       '5 0'] #29

n, k = map(int, inp[0].split())
data = []
for i in range(n):
    data.append(list(map(int, inp[1+i].split())))

def luckBalance(k, contests):
    nimp = []
    imp = []
    for el in contests:
        if not el[1]:
            nimp.append(el)
        else:
            imp.append(el)
    imp.sort()
    #sum_nimp = sum([x[0] for x in nimp])
    sum_nimp = sum([x[0] for x in nimp])
    sum_imp = sum([x[0] for x in imp])
    sub_imp = 0
    n = len(imp) - k
    if n:
        sub_imp = -2*sum([imp[i][0] for i in range(n)])
    return sum_nimp + sum_imp + sub_imp

print(luckBalance(k, data))