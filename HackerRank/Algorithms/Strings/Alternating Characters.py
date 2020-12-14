inp = ['5',
       'AAAA',
       'BBBBB',
       'ABABABAB',
       'BABABA',
       'AAABBB']

def alternatingCharacters(s):
    ch = s[0]
    counter = 1
    for char in s[1:]:
        if char != ch:
            counter += 1
            ch = char
    return len(s)-counter

for i in range(1, int(inp[0])+1):
    print(alternatingCharacters(inp[i]))