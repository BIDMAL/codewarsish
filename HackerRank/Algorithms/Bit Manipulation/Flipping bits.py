import operator
inp = ['3',
       '2147483647',
       '1',
       '0']

def flippingBits(n):
    return operator.xor(n, 4294967295)

q = int(inp[0])
for i in range(q):
    print(flippingBits(int(inp[1+i])))