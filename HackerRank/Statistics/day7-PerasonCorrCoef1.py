from math import sqrt

# n = int(input())
# X = list(map(float, input().split()))
# Y = list(map(float, input().split()))

n = 10
X = list(map(float, "10 9.8 8 7.8 7.7 7 6 5 4 2".split()))
Y = list(map(float, "200 44 32 24 22 17 15 12 8 4".split()))


def findMu(arr):
    return sum(arr)/len(arr)


def findSD(arr, mu):
    return sqrt(sum([(x - mu)**2 for x in arr]) / len(arr))


def findRo(X, Y, muX, sdX, muY, sdY, n):
    total = 0
    for i in range(len(X)):
        total += (X[i]-muX)*(Y[i]-muY)
    return total / (n*sdX*sdY)


muX = findMu(X)
muY = findMu(Y)
sdX = findSD(X, muX)
sdY = findSD(Y, muY)
ro = findRo(X, Y, muX, sdX, muY, sdY, n)

print(f'{ro:.3f}')
