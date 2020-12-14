inp = ["5 3",
       "10 2 5",
       "7 1 0",
       "9 9 9",
       "1 23 12",
       "6 5 9",
       "1"]
from operator import itemgetter
n, m = map(int, inp[0].split())
arr = []
for i in range(n):
       arr.append( list(map(int, inp[1+i].split())) )
k = int(inp[n+1])
for line in sorted(arr, key=lambda x: x[k]):
       print(*line)