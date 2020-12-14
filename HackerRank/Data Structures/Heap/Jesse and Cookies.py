inp = ['6 7',
       '1 2 3 9 10 12']

import heapq

n, k = map(int, inp[0].split())
A = list(map(int, inp[1].split()))

def cookies(k, A):
    heapq.heapify(A)
    ops = 0
    while len(A) > 1 and A[0] < k:
        x1 = heapq.heappop(A)
        x2 = heapq.heappop(A)
        heapq.heappush(A, x1 + 2*x2)
        ops += 1
    
    return ops if len(A) > 0 and A[0] >= k else -1

print(cookies(k, A))