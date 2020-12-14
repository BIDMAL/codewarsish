from functools import reduce
inp = ['2',
       '5',
       '0 2 3 0 6',
       '4',
       '0 0 0 0']

def pokerNim(c):
    cs = []
    for i in range(1,len(c)):
        cs.append(i if (c[i] % 2 == 1) else 0)
    if len(cs)>0:
        return reduce(lambda x, y: x ^ y, cs)
    else:
        return False

T = int(inp[0])
for i in range(T):
    n = int(inp[1+2*i])
    c = list(map(int, inp[2+2*i].split()))
    print('First' if pokerNim(c) else 'Second')
