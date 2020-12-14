inp = ['4',
       '1112',
       '1912',
       '1892',
       '1234']

n = int(inp[0])
grid = inp[1:]

def cavityMap(grid):
    grid2 = grid
    n = len(grid)
    for i in range(1, n-1):
        for j in range(1, n-1):
            if ((grid[i][j] > grid[i-1][j]) and (grid[i][j] > grid[i+1][j])
                and (grid[i][j] > grid[i][j-1]) and (grid[i][j] > grid[i][j+1])):
                grid2[i] = grid2[i][:j] + 'X' + grid2[i][j+1:]
    return(grid2)

print('\n'.join(cavityMap(grid)))