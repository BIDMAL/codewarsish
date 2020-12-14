inp = ['1',
       '5',
       'ebacd',
       'fghij',
       'olmkn',
       'trpqs',
       'xywuv']

def gridChallenge(grid):
    for line in grid:
        line.sort()
    t_grid = list(map(list, zip(*grid)))
    t_grid_s = []
    for line in t_grid:
        t_grid_s.append(sorted(line))
    return 'YES' if t_grid == t_grid_s else 'NO'

t = int(inp[0])
for i in range(t):
    n = int(inp[1+i])  # indexing is a placeholder here, not
    data = []
    for j in range(n):
        data.append([char for char in inp[2+i*n+j]])
    print(gridChallenge(data))