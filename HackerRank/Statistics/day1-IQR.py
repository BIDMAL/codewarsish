# n = int(input())
# vals = list(map(int, input().split()))
# freqs = list(map(int, input().split()))
vals = list(map(int, '6 12 8 10 20 16'.split()))
freqs = list(map(int, '5 4 3 2 1 5'.split()))

arr = []
for i, val in enumerate(vals):
    for _ in range(freqs[i]):
        arr.append(val)
arr.sort()

midp = len(arr)//2
arr1 = arr[:midp]
if len(arr) % 2 == 0:
    q2 = (arr[midp-1] + arr[midp])/2
    arr2 = arr[midp:]
else:
    q2 = arr[midp]
    arr2 = arr[midp+1:]

midp = len(arr1)//2
if len(arr1) % 2 == 0:
    q1 = (arr1[midp-1] + arr1[midp])/2
    q3 = (arr2[midp-1] + arr2[midp])/2
else:
    q1 = arr1[midp]
    q3 = arr2[midp]

print(f'{q3-q1:.1f}')
