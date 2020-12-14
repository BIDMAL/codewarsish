inp = ['10',
       'www.abc.xy',
       '87']

n = int(inp[0])
s = inp[1]
k = int(inp[2])

def CaesarCipher(s, k):
    al = 'abcdefghijklmnopqrstuvwxyz'
    alup = al.upper()
    cal = ''
    lal = len(al)
    for i in range(len(al)):
        cal += al[(i+k)%lal]
    calup = cal.upper()

    cs = ''
    for char in s:
        if char in cal:
            cs += cal[al.index(char)]
        elif char in calup:
            cs += calup[alup.index(char)]
        else:
            cs += char
    return(cs)

print(CaesarCipher(s, k))