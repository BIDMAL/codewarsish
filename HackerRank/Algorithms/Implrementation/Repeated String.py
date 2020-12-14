inp = ['a',
       '1000']

s = inp[0]
n = int(inp[1])

def repeatedString(s, n):
    ls = len(s)
    fulls = n // ls
    remsymb = n - fulls*ls
    return(s.count('a') * fulls + s[:remsymb].count('a'))

print(repeatedString(s, n))