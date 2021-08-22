from math import e

nu = 2.5
k = 5


def fact(x):
    if x == 0:
        return 1

    return x*fact(x-1)


p = nu**k * e**(-nu) / fact(k)

print(f'{p:.3f}')
