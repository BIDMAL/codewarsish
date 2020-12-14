inp = ['6',              
       'lmno',          # lmon
       'dcba',          # no answer
       'dcbb',          # no answer
       'abdc',          # acbd
       'abcd',          # abdc
       'fedcbabcd']     # fedcbabdc
# inp = ['5',
#        'ab',
#        'bb',
#        'hefg',
#        'dhck',
#        'dkhc']         # hcdk
inp = ['1',
       'fcakwzuqlzglnibqmkd']
      # fcakwzuqlzglnidbkmq
def biggerIsGreater(w):
    w = list(w)
    length = len(w)
    k = -1
    for i in range(length - 1):
        if w[i] < w[i+1]:
            k = i
            # would be better to make reverse search here, but cba atm
    if k >= 0:
        for i in range(1, length - k):
            if w[-i] > w[k]:
                w[-i], w[k] = w[k], w[-i]
                w[k+1:] = w[k+1:][::-1]
                break
    return 'no answer' if k == -1 else ''.join(w)

# n = int(input())
# f = open('log.txt', 'w')
# for i in range(n):
#     f.write(biggerIsGreater(input().strip()) + '\n')
# f.close()

n = int(inp[0])
for i in range(n):
    print(biggerIsGreater(inp[1+i].strip()))
