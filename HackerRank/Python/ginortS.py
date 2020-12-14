s = 'Sorting1234'
ods, eds, cs, ss = '', '', '', ''
for char in s:
    if char in '13579':
        ods += char
    elif char in 'ABCDEFGHIJKLMNOPQRSTUVWXYZ':
        cs += char
    elif char in 'abcdefghijklmnopqrstuvwxyz':
        ss += char
    else:
        eds += char
s = sorted(ss) + sorted(cs) + sorted(ods) + sorted(eds)
print(*s, sep='')
