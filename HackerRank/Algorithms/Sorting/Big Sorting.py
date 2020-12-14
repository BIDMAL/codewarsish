inp = ['6',
       '31415926535897932384626433832795',
       '1',
       '3',
       '10',
       '3',
       '5']

n = int(inp[0])
arr = []

for i in range(1, n+1):
    arr.append(int(inp[i]))

def bigSorting(unsorted):
    unsorted.sort(key=int)
    print(*unsorted, sep='\n')

bigSorting(arr)