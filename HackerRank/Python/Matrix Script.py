import re
l = ['7 3',
     'Ts^',
     'h%x',
     'i #',
     'sM ',
     '$a ',
     '#t%',
     'ir!']
l = ['5 9',
     '#%$r%r$n ',
     'O%Mi$iTi$',
     'yiaxsprt ',
     'est%ctiy#',
     '  t c i %']

first_multiple_input = l[0].rstrip().split()
                       
n = int(first_multiple_input[0])

m = int(first_multiple_input[1])

matrix = []
for i in range(n):
    matrix_item = l[i+1]
    matrix.append(matrix_item)

s = ''
for j in range(m):
    for i in range(n):
        s += matrix[i][j]

s2 = s
print(s)
for subs in re.findall(r'(?<=[A-Za-z0-9])[^A-Za-z0-9]+(?=[A-Za-z0-9])', s):
    s2 = s2.replace( str(subs), ' ', 1 )

print( ' '.join(s2.strip().split()) )