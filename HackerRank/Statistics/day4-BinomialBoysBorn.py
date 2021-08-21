# rb,rg = tuple(map(float, input().split()))
rb = 1.09
rg = 1

p = rb/(rb+rg)

def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f


def combs(n, k):
    return int(fact(n)/fact(k)/fact(n-k))


def binom(x, n, p):
    return combs(n, x)*(p**x)*((1-p)**(n-x))

atl3 = binom(3,6,p) + binom(4,6,p) + binom(5,6,p) + binom(6,6,p)

print(f'{atl3:.3f}')
