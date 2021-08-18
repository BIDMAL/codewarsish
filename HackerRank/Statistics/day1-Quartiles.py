# n = int(input())
# arr = list(map(int, input().split()))
arr = "3 7 8 5 12 14 21 13 18"
arr = list(map(int, arr.split()))
arr.sort()
print(arr)
n = len(arr)

midp = n//2
arr1 = arr[:midp]
if n%2 == 0:
    q2 = (arr[midp-1] + arr[midp])/2    
    arr2 = arr[midp:]
else:
    q2 = arr[midp]
    arr2 = arr[midp+1:]

midp = len(arr1)//2
if len(arr1)%2 == 0:
    q1 = (arr1[midp-1] + arr1[midp])/2    
    q3 = (arr2[midp-1] + arr2[midp])/2
else:
    q1 = arr1[midp]
    q3 = arr2[midp]

print(f'{int(q1)}')
print(f'{int(q2)}')
print(f'{int(q3)}')