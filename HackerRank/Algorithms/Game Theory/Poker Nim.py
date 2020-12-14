from functools import reduce
inp = ['2',
       '2 5',
       '1 2',
       '3 5',
       '2 1 3']

def pokerNim(k, c):
    
    return reduce(lambda x, y: x ^ y, c)

T = int(inp[0])
for i in range(T):
    n, k = map(int, inp[1+2*i].split())
    c = list(map(int, inp[2+2*i].split()))
    print('First' if pokerNim(k, c) else 'Second')


"""
from functools import reduce

def pokerNim(k, c):    
    return reduce(lambda x, y: x ^ y, c)

for _ in range(int(input())):
    n, k = map(int, input().split())
    c = list(map(int, input().split()))
    print('First' if pokerNim(k, c) else 'Second')"""