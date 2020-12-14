from collections import Counter
inp = ['4',
       '4',
       '1 1 0 0',
       '0 1 1 0',
       '0 0 1 0',
       '1 0 0 0']
inp = ['5',
       '4',
       '0 0 1 1',
       '0 0 1 0',
       '0 1 1 0',
       '0 1 0 0',
       '1 1 0 0']
inp = ['7',
       '5',
       '1 1 1 0 1',
       '0 0 1 0 0',
       '1 1 0 1 0',
       '0 1 1 0 0',
       '0 0 0 0 0',
       '0 1 0 0 0',
       '0 0 1 1 0']
inp = ['8',
       '9',
       '0 1 0 0 0 0 1 1 0',
       '1 1 0 0 1 0 0 0 1',
       '0 0 0 0 1 0 1 0 0',
       '0 1 1 1 0 1 0 1 1',
       '0 1 1 1 0 0 1 1 0',
       '0 1 0 1 1 0 1 1 0',
       '0 1 0 0 1 1 0 1 1',
       '1 0 1 1 1 1 0 0 0']

def connectedCell(matrix, r, c):
    rnmap = [[0 for _ in range(c)] for _ in range(r)]
    crn = 1 
    for i in range(r):
        for j in range(c):
            if matrix[i][j]:
                if i > 0 and j > 0 and rnmap[i-1][j-1]:
                    rnmap[i][j] = rnmap[i-1][j-1]
                elif i > 0 and rnmap[i-1][j]:
                    rnmap[i][j] = rnmap[i-1][j]
                elif j > 0 and rnmap[i][j-1]:
                    rnmap[i][j] = rnmap[i][j-1]
                elif j < (c-1) and rnmap[i][j+1]:
                    rnmap[i][j] = rnmap[i][j+1]
                elif i > 0 and j < (c-1) and rnmap[i-1][j+1]:
                    rnmap[i][j] = rnmap[i-1][j+1]
                else:
                    rnmap[i][j] = crn
                    crn += 1
    for i in range(r):
        k = sum([1 for el in rnmap[i] if el])
        for _ in range(k):
            for j in range(c):
                if j > 0 and rnmap[i][j-1]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i][j-1]) 
                if i > 0 and rnmap[i-1][j]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i-1][j])
                if j < c-1 and rnmap[i][j+1]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i][j+1])
                if i < r-1 and rnmap[i+1][j]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i+1][j])
                if i > 0 and j > 0 and rnmap[i-1][j-1]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i-1][j-1])
                if i > 0 and j < c-1 and rnmap[i-1][j+1]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i-1][j+1])
                if i < r-1 and j < c-1 and rnmap[i+1][j+1]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i+1][j+1])
                if i < r-1 and j > 0 and rnmap[i+1][j-1]:
                    rnmap[i][j] = min(rnmap[i][j], rnmap[i+1][j-1])
                

    print(*rnmap, sep='\n')
    return rnmap

r, c = int(inp[0]), int(inp[1])
M = []
for i in range(r):
    M.append(list(map(int, inp[2+i].split())))

rangemap = connectedCell(M, r, c)
cnt = Counter(x for xs in rangemap for x in list(xs) if x)
print(max(cnt.values()))
