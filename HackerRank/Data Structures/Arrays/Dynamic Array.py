inp = ['2 5',
       '1 0 5',
       '1 1 7',
       '1 0 3',
       '2 1 0',
       '2 1 1']

def dynamicArray(n, queries):
    seq = [[] for i in range(n)]
    lastAnswer = 0
    for quer in queries:
        x = quer[1]
        y = quer[2]
        ind = (x ^ lastAnswer) % n
        if quer[0] == 1:
            seq[ind].append(y)
        if quer[0] == 2:
            lastAnswer = seq[ind][y % len(seq[ind])]
            print(lastAnswer)
    return seq

n, q = map(int, inp[0].split())
queries = []
for i in range(q):
    queries.append(list(map(int, inp[1+i].split())))

dynamicArray(n, queries)