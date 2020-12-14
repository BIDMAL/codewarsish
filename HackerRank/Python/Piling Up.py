from collections import deque
n1 = 6
l1 = [4, 3, 2, 1, 3, 4]
n2 = 3
l2 = [1, 3, 2]

def pile(n, d):
    d = deque(d)
    cur = d[0]
    for i in range(n-1):
        if d[-1]>cur:
            cur = d[-1]
            d.pop()
        else:
            d.popleft()
        if (d[0] > cur) or (d[-1]>cur):
            return("No")  
    return("Yes")


print(pile(n1, l1))

     