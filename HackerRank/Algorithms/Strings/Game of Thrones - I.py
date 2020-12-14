from collections import Counter
inp = ['aaabbbb',
       'cdefghmnopqrstuvw',
       'cdcdcdcdeeeef']

def gameOfThrones(s):
    c = Counter(s)
    odd = 0
    for val in c.values():
        if val%2:
            odd += 1
        if odd > 1:
            return 'NO'
    return 'YES'

for i in range(len(inp)):
    print(gameOfThrones(inp[i]))