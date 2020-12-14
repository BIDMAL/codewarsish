inp = '1 2 4 4 4 4'
ar = list(map(int, inp.split()))
def pickingNumbers(a):
    s = list(set(a))
    n = len(s)
    ml = 0
    #if n == 1:
    #    ml = len(a)
    #else:
    for i in range(n):
        for j in range(i,n):
            if (abs(s[i]-s[j]) <= 1):
                l = (a.count(s[i]) + a.count(s[j])) // (1 + (s[i]==s[j]))
                ml = max(ml, l)    
    return(ml)
print(pickingNumbers(ar))