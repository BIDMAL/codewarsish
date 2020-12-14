inp = ['2',
       'acxz',
       'bcxz']

def IsItFunny(s):
    ln = len(s)
    lngts = []
    for i in range(ln-1):
        lngts.append( abs(ord(s[i+1]) - ord(s[i])) )
    return('Funny' if lngts[:] == lngts[::-1] else 'Not Funny')

for i in range(1, int(inp[0]) + 1):
    print(IsItFunny(inp[i]))