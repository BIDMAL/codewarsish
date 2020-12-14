inp = ['5',
       '12',
       '9 6 8 12 3 7 1 11 10 2 5 4',                            #       NO   
       '21',
       '17 21 2 1 16 9 12 11 6 18 20 7 14 8 19 10 3 4 13 5 15', #       YES
       '15',    
       '5 8 13 3 10 4 12 1 2 7 14 6 15 11 9',                   #       NO
       '13',
       '8 10 6 11 7 1 9 12 3 5 13 4 2',                         #       YES
       '18',
       '7 9 15 8 10 16 6 14 5 13 17 12 3 11 4 1 18 2']          #       NO

def rotateL3(abc):
    abc.append(abc.pop(0))
    return abc

def larrysArray(A):
    n = len(A)

    for i in range(1, n - 1):
        while A[i-1] != i:
            k = A.index(i) - 2
            if k == i - 3:
                continue
            ind = (i-1) if (k < (i-1)) else k
            while A[ind] != i:
                A[ind:ind+3] = rotateL3(A[ind:ind+3])
    res = (A[-2] == n-1) and (A[-1] == n) 
    return res

t = int(inp[0])
for i in range(t):
    n = int(inp[1 + i * 2])
    ar = list(map(int, inp[2 + i * 2].split()))
    print('YES' if larrysArray(ar) else 'NO')