inp = ['6',
       '1 4 3 5 6 2']

def insertionSort2(n, arr):
    for i in range(1, n):
        el = arr[i]
        del(arr[i])
        needed = True
        for j in range(i):
            if arr[j]>el:
                arr.insert(j, el)
                needed = False
                break
        if needed:
            arr.insert(i, el)
        print(*arr)

insertionSort2(int(inp[0]), list(map(int, inp[1].split())))