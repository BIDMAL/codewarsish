n = int(input())
X = list(map(int, input().split()))
W = list(map(int, input().split()))
w_sum = 0
wx_sum = 0

for i, w in enumerate(W):
    w_sum += w
    wx_sum += w*X[i]

print(f"{wx_sum/w_sum:.1f}")
