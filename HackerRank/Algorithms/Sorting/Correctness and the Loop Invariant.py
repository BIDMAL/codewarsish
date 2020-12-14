#inp = '2 1 3 1 2'
inp = '10 9 8 7 6 5 4 3 2 1'
def runningTime(arr):
    counter = 0    
    for i in range(1, len(arr)):
        j = i-1
        key = arr[i]
        while (j >= 0) and (arr[j] > key):
            arr[j+1] = arr[j]
            counter += 1
            j -= 1
        arr[j+1] = key    
    return counter

arr = list(map(int, inp.split()))
print(runningTime(arr))