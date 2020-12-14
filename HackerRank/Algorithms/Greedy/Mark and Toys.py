inp = ['7 50',
       '1 12 5 111 200 1000 10']

n, k = map(int, inp[0].split())
prices = list(map(int, inp[1].strip().split()))

def maximumToys(prices, k):
    total = 0
    res = 0
    for el in sorted(prices):
        total += el
        if total > k:
            break
        res += 1
    return res

print(maximumToys(prices, k))