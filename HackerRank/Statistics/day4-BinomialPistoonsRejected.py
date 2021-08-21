# perc, n = tuple(map(int, input().split()))
perc = 12
n = 10

p = perc/100


def fact(x):
    f = 1
    for i in range(1, x+1):
        f *= i
    return f


def combs(n, k):
    return int(fact(n)/fact(k)/fact(n-k))


def binom(x, n, p):
    return combs(n, x)*(p**x)*((1-p)**(n-x))


noMoreThan2 = binom(0, n, p) + binom(1, n, p) + binom(2, n, p)
atl2 = 1 - binom(0, n, p) - binom(1, n, p)


print(f'{noMoreThan2:.3f}')
print(f'{atl2:.3f}')
