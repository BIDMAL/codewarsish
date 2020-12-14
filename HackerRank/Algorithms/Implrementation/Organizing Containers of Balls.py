inp = ['2',
       '3',
       '1 3 1',
       '2 1 2',
       '3 3 3',
       '3',
       '0 2 1',
       '1 1 1',
       '2 0 0']

def organizingContainers(container):
    types = []
    baskets = []
    for basket in container:
        baskets.append(sum(basket))

    for typ in zip(*container):
        types.append(sum(typ))
    return 'Possible' if sorted(types) == sorted(baskets) else 'Impossible'

q = int(inp[0])
k = 1
for i in range(q):
    container = []
    n = int(inp[k])
    k += 1
    for j in range(n):
        container.append(list(map(int, inp[k+j].split())))
    k += n
    print(organizingContainers(container))