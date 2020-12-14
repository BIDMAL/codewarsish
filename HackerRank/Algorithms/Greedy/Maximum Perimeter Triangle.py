inp = ['6',
       '1 1 1 2 3 5']

data = list(map(int, inp[1].split()))

def maximumPerimeterTriangle(sticks):
    sticks.sort(reverse=True)
    res = [-1]
    for i in range(len(sticks)-2):
        if sticks[i] < sticks[i+1] + sticks[i+2]:
            res = sticks[i:i+3]
            break
    return sorted(res)

print(*maximumPerimeterTriangle(data))
