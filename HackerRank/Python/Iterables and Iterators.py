import itertools as iter

n = 4 
inp = 'a a c d'.split()
k = 2
combs = [comb for comb in iter.combinations(inp, k)]
a = 0
for comb in combs:
    if 'a' in comb:
        a += 1
print("{0:.4f}".format(a/len(combs)))