inp = ['5',
       '8 1',
       '4 2',
       '5 6',
       '3 1',
       '4 3']

n = int(inp[0])
customers = []
for i in range(n):
    customers.append(list(map(int, inp[1+i].split())))

def jimOrders(orders):
    servs = [(idx+1, sum(order)) for idx, order in enumerate(orders)]
    servs.sort(key=lambda x: x[1])
    return [serv[0] for serv in servs]

print(*jimOrders(customers))
