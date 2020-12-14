inp = ['2',
       '4',
       '5',
       '1 4 5 3 2',
       '4',
       '4',
       '2 2 4 3']

t = int(inp[0])
def icecreamParlor(m, arr):
    res = []
    found = False
    for i in range(len(arr)-1):
        if found:
            break
        if arr[i] < m:
            for j in range(i+1, len(arr)):
                if arr[i]+arr[j] == m:
                    res = [i+1, j+1]
                    break
    return sorted(res)

for i in range(t):
    m = int(inp[1+i*3])
    n = int(inp[2+i*3])
    arr = list(map(int, inp[3+i*3].split()))
    print(*icecreamParlor(m, arr))