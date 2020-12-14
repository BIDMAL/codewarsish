inp = ['4',
       '1 4 3 2']

def reverseArray(a):
    return a[::-1]

N = int(inp[0])
arr = list(map(int, inp[1].split()))

print(*reverseArray(arr))

