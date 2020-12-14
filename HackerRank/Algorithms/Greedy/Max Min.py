inp = ['7',
       '3',
       '10',
       '100',
       '300',
       '200',
       '1000',
       '20',
       '30']

inp = ['7',
       '3',
       '100',
       '200',
       '300',
       '350',
       '400',
       '401',
       '402']

n = int(inp[0])
k = int(inp[1])
arr = []
for i in range(n):
    arr.append(int(inp[2+i]))

def maxMin(k, arr):
    arr.sort()
    unf = max(arr) - min(arr)
    for i in range(len(arr) - k + 1):
        unf = min(unf, arr[i+k-1] - arr[i])
    return unf

print(maxMin(k, arr))
