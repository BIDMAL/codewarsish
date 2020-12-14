inp = '3 3 2 1 3'
arr = list(map(int, inp.split()))

def equalizeArray(arr):
    uniq = set(arr)
    maxoc = 0
    for el in uniq:
        if arr.count(el) > maxoc:
            maxoc = arr.count(el)
    return(len(arr) - maxoc)

print(equalizeArray(arr))