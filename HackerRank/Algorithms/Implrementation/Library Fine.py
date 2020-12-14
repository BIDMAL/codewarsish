inp = ['9 6 2015',
       '6 6 2015']
inp = ['2 7 1014',
       '1 1 1015']

ret = list(map(int, inp[0].split()))
exp = list(map(int, inp[1].split()))

def libraryFine(d1, m1, y1, d2, m2, y2):
    if y1 > y2:
        return(10000)
    elif (y1 == y2) and (m1 > m2):
        return((m1-m2)*500)
    elif (y1 == y2) and (m1 == m2) and (d1 > d2):
        return((d1-d2)*15)
    else:
        return(0)

print(libraryFine(ret[0], ret[1], ret[2], exp[0], exp[1], exp[2]))