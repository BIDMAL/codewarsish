inp = ['3 2 3',
       '1 2 3',
       '0',
       '1',
       '2']

a = list(map(int, inp[1].split()))
k = int((inp[0].split()[1]))
quiries = [int(x) for x in inp[2:]]


def circularArrayRotation(a, k, queries):
    l = k%len(a)
    a = a[-l:] + a[:-l]
    return([a[i] for i in queries])

print(circularArrayRotation(a, k, quiries))