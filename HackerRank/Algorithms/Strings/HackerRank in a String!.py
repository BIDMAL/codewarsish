inp = 'hhaacckkekraraannk'
inp2 = 'hackerworld'

def StringContainsHR(s):
    res = True
    ind = 0
    for char in 'hackerrank':
        f = s[ind:].find(char)
        if f == -1:
            res = False
            break
        else:
            ind = ind + f + 1
    return 'YES' if res else 'NO' 

print(StringContainsHR(inp))