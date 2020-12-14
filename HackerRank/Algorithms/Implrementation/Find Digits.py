def findDigits(n):
    res = 0
    for i in str(n):
        if i != '0':
            res += (n%int(i)==0)
    return(res)

print(findDigits(1012))