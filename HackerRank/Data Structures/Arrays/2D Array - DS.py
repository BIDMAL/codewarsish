inp = ['-1 -1 0 -9 -2 -2',
       '-2 -1 -6 -8 -2 -5',
       '-1 -1 -1 -2 -3 -4',
       '-1 -9 -2 -4 -4 -5',
       '-7 -3 -3 -2 -9 -9',
       '-1 -3 -1 -2 -4 -5']

def hourglassSum(arr):
    n = len(arr)
    ms = None
    for i in range(n-2):
        for j in range(n-2):
            s = arr[i][j] + arr[i][j+1] + arr[i][j+2] + arr[i+1][j+1] + \
                arr[i+2][j] + arr[i+2][j+1] + arr[i+2][j+2]
            if ms is not None:
                ms = max(ms, s)
            else:
                ms = s
    return ms

arr = [list(map(int, inp[0].split()))]
for i in range(len(arr[0])-1):
    arr.append(list(map(int, inp[1+i].split())))

print(hourglassSum(arr))