inp = ['5 1',
       '4 2 3 5 1']

n, k = map(int, inp[0].split())
arr = list(map(int, inp[1].split()))

def largestPermutation(k, arr):
    d = {k:v for v, k in enumerate(arr)}
    i = 0
    m = len(arr)
    while k > 0 and m > 1:
        if arr[i] != m:
            arr[i], arr[d[m]] = arr[d[m]], arr[i]
            d[arr[d[m]]], d[m] = d[m], i          
            k -= 1
        m -= 1
        i += 1
    return arr

print(*largestPermutation(k, arr))