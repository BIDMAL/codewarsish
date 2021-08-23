mu, sigma = 500, 80

muS, sigmaS = mu, sigma/(100**0.5)

A = mu - (1.96*sigmaS)
B = mu + (1.96*sigmaS)

print(round(A, 2))
print(round(B, 2))
