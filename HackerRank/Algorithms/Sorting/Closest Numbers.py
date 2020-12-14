#inp = ['10',
#       '-20 -3916237 -357920 -3620601 7374819 -7330761 30 6246457 -6461594 266854']
#
#n = int(inp[0])
#arr = list(map(int, inp[1].split()))

with open('D:/Pp/HackerRank/Algorithms/Sorting/closestnumbersT3.txt') as f:
    n = int(f.readline())
    arr = list(map(int, f.readline().split()))

def closestNumbers(arr):
    
    sarr = sorted(arr)
    cns = [min(sarr[0], sarr[1]), max(sarr[0], sarr[1])]
    min_val = abs(sarr[0] - sarr[1]) 
    for i in range(2, len(arr)):
        dif_val = abs(sarr[i] - sarr[i-1])
        if dif_val == min_val:
            cns.extend([min(sarr[i], sarr[i-1]), max(sarr[i], sarr[i-1])])
        elif dif_val < min_val:
            min_val = dif_val
            cns = [min(sarr[i], sarr[i-1]), max(sarr[i], sarr[i-1])]
    return cns

print(*closestNumbers(arr))