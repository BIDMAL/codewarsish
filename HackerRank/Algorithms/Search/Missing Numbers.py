inp = ['10',
       '203 204 205 206 207 208 203 204 205 206',
       '13',
       '203 204 204 205 206 207 205 208 203 206 205 206 204']

n1 = int(inp[0])
arr1 = list(map(int, inp[1].split()))
n2 = int(inp[2])
arr2 = list(map(int, inp[3].split()))

def missingNumbers(arr, brr):
    res = []
    for el in brr:
        if el not in arr:
            res.append(el)
        else:
            arr.remove(el)
    return sorted(set(res))

print(*missingNumbers(arr1, arr2))