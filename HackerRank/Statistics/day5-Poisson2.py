nuA = 0.88
nuB = 1.55

eA = 160 + 40 * (nuA + nuA**2)
eB = 128 + 40 * (nuB + nuB**2)

print(f'{eA:.3f}')
print(f'{eB:.3f}')
