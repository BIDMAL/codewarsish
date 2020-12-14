from operator import xor


a = 5
b = 6

def maximizingXor(l, r):
    mx = 0
    for i in range(l, r):
        for j in range(i+1, r+1):
            mx = max(mx, xor(i, j))
    return mx

print(maximizingXor(a, b))