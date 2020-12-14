inp = ['4',
       'abc',
       'abcba',
       'abcd',
       'cba']

def theLoveLetterMystery(s):
    ln = len(s)
    n = ln // 2
    l = [ord(char) for char in s[0:n]]
    r = [ord(char) for char in s[:ln-n-1:-1]]
    return(sum([ abs(l[i] - r[i]) for i in range(n) ]))

for i in range(1, int(inp[0])+1):
    print(theLoveLetterMystery(inp[i]))