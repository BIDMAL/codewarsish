import re

inp = ['11',
       'AUzs-nV']

n = int(inp[0])
pwd = inp[1]

def VerifyStrongReq(pwd):
    lenreq = 6 - len(pwd)
    dreq = len(re.findall(r'[0-9]', pwd)) == 0
    lcreq = len(re.findall(r'[a-z]', pwd)) == 0
    ucreq = len(re.findall(r'[A-Z]', pwd)) == 0
    ssreq = len(re.findall(r'[!@#$%^&*()+-]', pwd)) == 0
    return(max(lenreq, dreq+lcreq+ucreq+ssreq))

print(VerifyStrongReq(pwd))