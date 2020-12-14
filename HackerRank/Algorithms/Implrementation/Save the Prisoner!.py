inp = '7 14 1'
n, m, s = map(int, inp.split())

def saveThePrisoner(n, m, s):    
    return( 1+ (n+s+m%n-2)%n)

print(saveThePrisoner(n, m, s))