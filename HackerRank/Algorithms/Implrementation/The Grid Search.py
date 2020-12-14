def gridSearch(G, P):
    found = False
    gs = len(G)
    ps = len(P)
    pls = len(P[0])
    for ind, line in enumerate(G):
        if (P[0] in line) and (ind+ps <= gs):
            found = True
            lind = line.find(P[0])
            for pind, pline in enumerate(P):
                if pline not in G[ind+pind][lind:lind+pls]:
                    found = False
                    break
        if found:
            break
    return 'YES' if found else 'NO'

T = int(input())
for _ in range(T):
    R, C = map(int, input().split())
    M = []
    for _ in range(R):
        M.append(input())
    r, c = map(int, input().split())
    P = []
    for _ in range(r):
        P.append(input())
    print(gridSearch(M, P))