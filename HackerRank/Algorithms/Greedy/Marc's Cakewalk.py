inp = ['3',
       '1 3 2']
n = int(inp[0])
data = list(map(int, inp[1].split()))

def marcsCakewalk(calorie):
    calorie.sort(reverse=True)
    return sum([2**i*calorie[i] for i in range(len(calorie))])

print(marcsCakewalk(data))