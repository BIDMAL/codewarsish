import itertools as it
inp = ['7 3',
       '1 2 4 5 7 8 10']
d = int(inp[0].split()[1])
arr = list(map(int, inp[1].split()))

#def beautifulTriplets(d, arr):
#    counter = 0
#    for i in range(len(arr)-2):
#        for j in range(i+1, len(arr)-1):
#            if arr[j]-arr[i]==d:
#                for k in range(j+1, len(arr)):
#                    if arr[k]-arr[j]==d:
#                        counter += 1
#    return(counter)
def beautifulTriplets(d, arr):
    gc = 0
    for i in range(len(arr)-2):
        if arr[i]+d in arr and arr[i]+2*d in arr:
            gc+=1
    return(gc)


print(beautifulTriplets(d, arr))