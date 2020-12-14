from os.path import abspath, exists

inp = ['4 5',
       '10101',
       '11100',
       '11010',
       '00101']

n, m = map(int, inp[0].split())
topic = inp[1:]

def acmTeam(topic):
    nts = len(topic[0])
    tsmax = 0
    ntms = 0
    n = len(topic)
    for i in range(n-1):
        for j in range(i+1,n):
            combined = str(int(topic[i]) + int(topic[j]))
            teamts = nts - combined.count('0') - (nts-len(combined))
            if teamts > tsmax:
                ntms = 1
                tsmax = teamts
            elif teamts == tsmax:
                ntms += 1
    return([tsmax, ntms])

result = acmTeam(topic)
print('\n'.join(map(str, result)))
