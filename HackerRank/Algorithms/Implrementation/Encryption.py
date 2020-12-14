import math
from functools import reduce
inp = 'feed thedog    '
inp = 'chillout'
def encryption(s):
    line = s.strip().replace(' ', '')
    size = math.sqrt(len(line))
    c = math.ceil(size)
    r = math.floor(size)
    if r*c < len(line):
        r = c
    line = line + ' '*(c**2 - len(line))
    
    ar = []
    for i in range(r):
        ar.append(line[c*i:c*(i+1)])
    
    res = ''
    for line in zip(*ar):

        res += ' ' + reduce((lambda x, y: str(x) + str(y)), line).replace(' ', '')
    return res.strip()

print(encryption(inp))