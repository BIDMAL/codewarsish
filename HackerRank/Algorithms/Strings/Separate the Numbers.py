import math
inp = ['7',
       '1234',
       '91011',
       '99100',
       '101103',
       '010203',
       '13',
       '1']

def IsSeparateBeautiful(s):
    ls = len(s)
    res = False
    f = s[0]
    if ls == 1 or f == '0':
        print('NO')
        return 
    for i in range(1, math.ceil(ls/2)+1):
        f = cur = s[:i]
        ind = i
        res = s[i] != '0'
        while (ind < ls) and res:
            if int(cur) == int(s[ind:ind+i]) - 1:
                cur = s[ind:ind+i]
            elif int(cur) == int(s[ind:ind+i+1]) - 1:
                cur = s[ind:ind+i+1]
                i += 1                
            else:
                res = False
                break
            ind += i           
        if res:
            break
    if res:        
        print('YES', f)
    else:
        print('NO')

for i in range(int(inp[0])):
    IsSeparateBeautiful(inp[i+1])