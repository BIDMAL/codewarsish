inp = ['hackerhappy',
       'hackerrank',
       '9']
inp = ['y',
       'yu',
       '2']
inp = ['aba',
       'aba',
       '7']
inp = ['abcd',
       'abcdert',
       '10']

def appendAndDelete(s, t, k):
    x = len(s)
    y = len(t)
    z = min(x,y)
    i = 0
    for i in range(z):
        if s[:z-i] == t[:z-i]:
            break
    req = x - (z - i) + (y - z) + i
    if req > k:
        return('No')
    elif (k-req)%2 == 0:
        return('Yes')
    elif (x-i+y)<(k-i):
        return('Yes')
    else:
        return('No')
    #return('Yes' if req <= k else 'No')

print(appendAndDelete(inp[0], inp[1], int(inp[2])))
