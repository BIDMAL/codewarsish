inp = ['2',
       '3',
       '1 2 3',
       '4',
       '1 2 3 3']

def balancedSums(arr):
    l = 0
    r = sum(arr)
    for i in range(len(arr)):
        r -= arr[i]
        if l == r:
            return('YES')
        l += arr[i]
    return('NO')

t = int(inp[0])
for i in range(t):
    n = inp[1+i*2]
    arr = list(map(int, inp[2+i*2].split()))
    print(balancedSums(arr))


