inp = ['5 3 4',
       '3 2 1 1 1',
       '4 3 2',
       '1 1 4 1']

n = list(map(int, inp[0].split()))
stacks = []
stacks.append(list(map(int, inp[1].split())))
stacks.append(list(map(int, inp[2].split())))
stacks.append(list(map(int, inp[3].split())))
lns = []
for i in range(3):
    lns.append(sum(stacks[i]) if len(stacks[i]) else 0)

while min(lns) != max(lns):
    i = lns.index(max(lns))
    z = stacks[i].pop(0)
    lns[i] -= z

print(lns[0])