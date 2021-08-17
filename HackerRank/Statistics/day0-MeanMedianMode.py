from scipy.stats import mode

n = int(input())
arr = list(map(int, input().split()))

arr.sort()
mean = sum(arr)/n
midp = n//2
if n % 2 == 0:
    median = (arr[midp]+arr[midp-1])/2
else:
    median = arr[midp]
moda = mode(arr)

print(f"{mean:.1f}")
print(f"{median:.1f}")
print(f"{moda[0][0]}")
