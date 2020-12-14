
inp = ['12',
       '1 3',
       '1 65',
       '2 65',
       '3',
       '2 3',
       '1 7',
       '3',
       '1 -1',
       '3',
       '2 -1',
       '3',
       '2 7']
inp = ['5',
       '1 4',
       '1 9',
       '3',
       '2 4',
       '3']

nq = int(inp[0])
mmin = None
mh = []
for i in range(nq):
    q = list(inp[1+i].split())
    if q[0] == '1':
        mh.append(int(q[1]))
        if mmin is None:
            mmin = q[1]
        elif int(q[1]) < int(mmin):
            mmin = q[1]
    elif q[0] == '2':
        mh.remove(int(q[1]))
        if len(mh) == 0:
            mmin = None
        elif q[1] == mmin:
            mmin = str(min(mh))
    if q[0] == '3':
        print(mmin)