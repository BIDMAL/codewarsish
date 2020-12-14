inp = ['8',
       '1',
       '3',
       '4',
       '5',
       '8',
       '9',
       '10',
       '11']
inp = ['10',
       '1',
       '2',
       '10',
       '100',
       '100',
       '200',
       '1',
       '1',
       '1',
       '1']

def decentNumber(n):
    if n < 3:
        return -1
    elif n%3 == 0:
        return '5'*n
    else:
        i5 = n//5
        s3 = 0
        s5 = 0
        for i in range(i5+1):
            if (n - 5*i)%3 == 0:
                s3 = 5*i
                s5 = n-s3
                break
        if s3 or s5:
            return '5'*s5 + '3'*s3
        else:
            return -1


t = int(inp[0])
for i in range(t):
    print(decentNumber(int(inp[1+i])))