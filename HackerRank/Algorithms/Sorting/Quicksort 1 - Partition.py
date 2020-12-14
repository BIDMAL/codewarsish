inp = '4 5 3 7 2'

def quickSortPart(arr):
    p = [arr[0]]
    l = []
    r = []
    for i in range(1, len(arr)):
        if arr[i] > p[0]:
            r.append(arr[i])
        elif arr[i] < p[0]:
            l.append(arr[i])
        else:
            p.append(arr[i]) 
    print(*l, *p, *r, sep=' ')
arr = list(map(int, inp.split()))
quickSortPart(arr)