from itertools import groupby
s = '1222311'

# l = [c[0] for c in groupby(s)]
# i = 0
# for n in range(len(l)):
#     if n == len(l) - 1:
#         e = len(s)
#     else:
#         e = i + s[i:].index(l[n+1])
#     print( (s[i:e].count(l[n]), int(l[n])), end=' ')
#     i = e

print(*[(len(list(c)), int(k)) for k, c in groupby(s)])