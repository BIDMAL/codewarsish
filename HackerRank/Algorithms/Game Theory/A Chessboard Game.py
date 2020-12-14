inp = ['3',
       '5 2',
       '5 3',
       '8 8']
#Second
#First
#First
def chessboardGame(x, y):
    if x % 4 in [1, 2] and y % 4 in [1, 2]:
        return False
    else:
        return True

t = int(inp[0])
for i in range(t):
    x, y = map(int, inp[1+i].split())
    print('First' if chessboardGame(x, y) else 'Second')