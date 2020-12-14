inp = ['2',
       '3 10',
       '2 1 3',
       '7 8 9',
       '4 5',
       '1 2 2 1',
       '3 3 3 4']

q = int(inp[0])

def twoArrays(k, A, B):
    res = True
    A.sort()
    B.sort(reverse=True)
    for i in range(len(A)):
        if A[i] + B[i] < k:
            res = False
            break
    return 'YES' if res else 'NO'

for i in range(q):
    n, k = map(int, inp[1+i*3].split())
    A = list(map(int, inp[2+i*3].split()))
    B = list(map(int, inp[3+i*3].split()))
    print(twoArrays(k, A, B))