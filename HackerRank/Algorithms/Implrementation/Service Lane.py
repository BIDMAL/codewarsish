inp = ['8 5',
       '2 3 1 2 3 2 3 3',
       '0 3',
       '4 6',
       '6 7',
       '3 5',
       '0 7']

n, t = map(int, inp[0].split())
width = list(map(int, inp[1].split()))
cases = []
for i in range(t):
    cases.append(list(map(int, inp[2+i].split())))

def serviceLane(n, cases):
    res = []
    for case in cases:
        res.append(min(width[case[0]:case[1]+1]))
    return(res)

result = serviceLane(n, cases)
print('\n'.join(map(str, result))) 