inp = ['2',
       '2 2',
       '1 4']

def towerBreakers(n, m):
    if m == 1:
        return 2
    elif n % 2 == 1:
        return 1
    else:
        return 2

t = int(inp[0])
for i in range(t):
    n, m = map(int, inp[1+i].split())
    print(towerBreakers(n, m))
