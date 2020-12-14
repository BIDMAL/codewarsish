inp = ['2',
       '2',
       '1 1',
       '3',
       '2 1 3']
from functools import reduce
def nimGame(piles):
    count_non_0_1 = sum(1 for x in piles if x > 1)
    is_near_endgame = (count_non_0_1 <= 1)
    if is_near_endgame:
        moves_left = sum(1 for x in piles if x > 0)
        is_odd = (moves_left % 2 == 1)
        sizeof_max = max(piles)
        if sizeof_max == 1 and is_odd:
            return False
        else:
            return True            
    return reduce(lambda x, y: x^y, piles)

g = int(inp[0])
for i in range(g):
    n = int(inp[1+2*i])
    piles = list(map(int, inp[2+2*i].split()))
    print('First' if nimGame(piles) else 'Second')