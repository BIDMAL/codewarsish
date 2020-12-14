inp = ['4',
       '7',
       'RBY_YBR',
       '6',
       'X_Y__X',
       '2',
       '__',
       '6',
       'B_RRBR']

def SolveLadyBugs(n, board):
    colors = set(board)
    if colors == {'_'}:
        return('YES')
    if '_' not in colors:
        if len(board) > 1:
            if len(board) > 2:
                answer = 'YES'
                for i in range(1, len(board)-2):
                    if board[i-1] != board[i] and board[i+1] != board[i]:
                        answer = 'NO'
                        break
                for char in colors:
                    if board.count(char) == 1:
                        answer = 'NO'
                        break
                return(answer)
            elif len(colors) == 1:
                return('YES')
            else:
                return('NO')
        else:
            return('NO')
    else:
        answer = 'YES'
        for char in colors:
            if char != '_' and board.count(char) == 1:
                answer = 'NO'
                break    
        return(answer)

t = int(inp[0])
for i in range(t):
    n = int(inp[1+2*i])
    board = [ char for char in inp[2+2*i] ]
    print(SolveLadyBugs(n, board))