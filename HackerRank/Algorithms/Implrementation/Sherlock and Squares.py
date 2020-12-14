import math
inp = ['2',
       '3 9',
       '17 24']

def squares(a, b):
    x = math.ceil(math.sqrt(a))
    y = math.floor(math.sqrt(b))
    return(len(list(range(x, y+1))))

for i in range(int(inp[0])):
    line = list(map(int, inp[i+1].split()))
    print(squares(line[0], line[1]))