inp = ['10',
       '-59 -36 -13 1 -53 -92 -2 -96 -54 75']

n = int(inp[0])
data = list(map(int, inp[1].split()))

def minimumAbsoluteDifference(arr):
    arr.sort()
    min_dif = abs(arr[0] - arr[-1])
    for i in range(0, len(arr) - 1):
        min_dif = min(min_dif, abs(arr[i] - arr[i+1]))
    return min_dif 

print(minimumAbsoluteDifference(data))