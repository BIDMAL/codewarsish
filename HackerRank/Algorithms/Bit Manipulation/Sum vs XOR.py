inp = 10000000

def sumXor(n):
    return 2**(bin(n)[2:].count('0')) if n else 1

print(sumXor(inp))                                                     
