inp = ['8',
       '1 2 3 21 7 12 14 21']

def toys(w):
    w.sort()
    counter = 1
    minw = w[0]
    newmw = False
    for i in range(1, len(w)):
        if newmw:
            minw = w[i-1]
            newmw = False
        if w[i] > minw + 4:
            counter += 1
            newmw = True
    return counter

n = int(inp[0])
data = list(map(int, inp[1].split()))
print(toys(data))