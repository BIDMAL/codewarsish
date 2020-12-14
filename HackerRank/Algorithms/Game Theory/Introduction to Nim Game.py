inp = ['2',
       '2',
       '1 1',
       '3',
       '2 1 4']
from functools import reduce
def nimGame(piles):            
    return reduce(lambda x, y: x^y, piles)

g = int(inp[0])
for i in range(g):
    n = int(inp[1+2*i])
    piles = list(map(int, inp[2+2*i].split()))
    print('First' if nimGame(piles) else 'Second')