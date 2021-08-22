import math
mean = 20.0
stddev = 2.0
h1 = 19.5
h21, h22 = 20.0, 22.0


def phi(b): return (1 + math.erf((b-mean) / (stddev * 2**0.5)))/2


lesh1 = phi(h1) - phi(0.0)
beth1h2 = phi(h22) - phi(h21)
print(f'{lesh1:.3f}')
print(f'{beth1h2:.3f}')
