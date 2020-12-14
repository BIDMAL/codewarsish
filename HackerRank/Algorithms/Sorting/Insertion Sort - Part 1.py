inp = ['10',
       '2 3 4 5 6 7 8 9 10 1']

def insertionSort1(n, arr):
    ins = arr[n-1]
    found = True
    for i in range(n-1):
        if arr[n-2-i] > ins:
            arr[n-1-i] = arr[n-2-i]
            print(*arr)
        else:
            arr[n-1-i] = ins
            print(*arr)
            found = False
            break
    if found:
        arr[0] = ins
        print(*arr)
    return

insertionSort1(int(inp[0]), list(map(int, inp[1].split())))