inp = ['8',
       '1',
       '2',
       '3',
       '4',
       '5',
       '6',
       '7',
       '10']
"""
Second
First
First
First
First
First
Second
First"""
inp = ['5',
       '10',
       '55',
       '11',
       '34',
       '92']
#inp = ['1', '55']
def gameOfStones(n):
    return n%7 >= 2

for i in range(int(inp[0])):
    print(gameOfStones(int(inp[1+i])))