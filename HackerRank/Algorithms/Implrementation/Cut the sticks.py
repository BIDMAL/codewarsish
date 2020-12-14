inp = '1 2 3 4 3 3 2 1'
arr = list(map(int, inp.split()))

def cutTheSticks(arr):
    res = [len(arr)]
    while arr.count(min(arr)) != len(arr):
        rem = min(arr)
        arr = [ (x - rem) for x in arr if x > rem ]
        res.append(len(arr))
    return(res)

print(*cutTheSticks(arr), sep='\n')