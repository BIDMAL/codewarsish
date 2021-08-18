from math import sqrt

n = int(input())
arr = list(map(int, input().split()))

mean = sum(arr)/n
sqd = 0
for x in arr:
    sqd += (mean-x)**2
std = sqrt(sqd/n)

print(f'{std:.1f}')
