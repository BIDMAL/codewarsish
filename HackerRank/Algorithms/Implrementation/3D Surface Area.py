inp = ['3 3',
       '1 3 4',
       '2 2 3',
       '1 2 4']

# inp = ['1 1',
#        '1']

# inp = ['2 2',
#        '1 3',
#        '2 1']

H, W = map(int, inp[0].split())
A = []
for i in range(H):
    A.append(list(map(int, inp[1+i].split())))

def surfaceArea(A):
    total = 0
    commons = 0
    for i in range(len(A)):
        for j in range(1, len(A[0])):
            commons += min(A[i][j], A[i][j-1])
    for i in range(len(A[0])):
        for j in range(1, len(A)):
            commons += min(A[j][i], A[j-1][i])

    for i in range(len(A)):
        for j in range(len(A[0])):
            total += A[i][j] * 4 + 2
    return total - commons * 2

print(surfaceArea(A))