n = 3
arrs = '1 1 2'
import operator
from functools import reduce
arr = list(map(int, arrs.split()))

def lonelyinteger(a):
    return reduce(operator.xor, a)

print(lonelyinteger(arr))