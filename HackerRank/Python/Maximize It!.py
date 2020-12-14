# k, m = map(int, input().split())
# l = [list(map(int, input().split())) for _ in range(k)]
# l = ['3 1000',
#      '2 5 4',
#      '3 7 8 9',
#      '5 5 7 8 9 10']

l = ['2 24',
     '3 24 48 96',
     '4 24 48 96 24']

k, m = map(int, l[0].split())
l = [list(map(int, s[1:].split())) for s in l[1:]]


from itertools import product
import math
p = list(product(*l))
s = 0
for prod in p:
    prodsq = tuple(x*x for x in prod)
    
    s = max(s, sum(prodsq)%m)
    print(prod, s)
print(s)

#my_list = [tuple(y * 100 for y in x ) for x in my_list]
from itertools import product

#k, m = map(int, input().split())
#n = (list(map(int, input().split()))[1:] for _ in range(k))
#results = map(lambda x: sum(i**2 for i in x) % m, product(*n))
#print(max(results))