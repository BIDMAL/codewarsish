import itertools
inp = 'asvkugfiugsalddlasguifgukvsa'

def ReduceToTwo(s):
    cs = list(set(s))
    ssl = []
    for pair in itertools.combinations(cs, 2):
        rs = [char for char in s if char in pair]
        valid = True
        for i in range(len(rs)-1):
            if rs[i] == rs[i+1]:
                valid = False
                break
        if valid:
            ssl.append(len(rs))
    if len(ssl):
        return(max(ssl))
    else:
        return(0)
print(ReduceToTwo(inp))