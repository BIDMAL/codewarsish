import math
inp = ['5 3',
       '4 2 6 1 10']

inp = ['10 5',
       '3 8 15 11 14 1 9 2 24 31']
n, k = map(int, inp[0].split())
arr = list(map(int, inp[1].split()))

def workbook(n, k, arr):
    page = 1
    counter = 0
    for chapter in arr:
        prob = 1
        for _ in range(math.ceil(chapter / k)):
            if page in range(prob, min(prob+k,chapter+1)):
                counter += 1
            prob += k
            page += 1
    return(counter)

print(workbook(n, k, arr))
