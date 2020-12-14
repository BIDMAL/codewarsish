inp = '20 3 6 85'
p, d, m, s = map(int, inp.split())

def howManyGames(p, d, m, s):
    counter = 0
    cost = p + d
    while s > 0:
        cost = cost - d
        cost = max(cost, m)
        if cost <= s:
            counter += 1
        s -= cost
    return(counter)

print(howManyGames(p, d, m, s))