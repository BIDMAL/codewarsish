inp = ['aaabbbbcccddd',
       '5',
       '9',
       '7',
       '8',
       '12',
       '5']

s = inp[0]
queries = []
for q in inp[2:]:
    queries.append(int(q))

def weightedUniformStrings(s, queries):
    weights = set()
    alph = '0abcdefghijklmnopqrstuvwxyz'
    cw = alph.index(s[0])
    weights.add(cw)
    for i in range(1,len(s)):
        cw = cw*(s[i] == s[i-1]) + alph.index(s[i])
        weights.add(cw)

    return [ 'Yes' if q in weights else 'No' for q in queries ]

print(*weightedUniformStrings(s, queries), sep='\n')