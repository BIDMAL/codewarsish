inp = ['5 4',
       '1 2 3 4 5']

def rotateLeft(d, arr):
    z = d % len(arr)
    return arr[z:] + arr[:z]

n, d = map(int, inp[0].split())
arr = list(map(int, inp[1].split()))

print(*rotateLeft(d, arr))