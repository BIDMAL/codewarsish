arr = '2 4'
brr = '16 32 96'
arr = list(map(int, arr.split()))
brr = list(map(int, brr.split()))

def getTotalX(a, b):
    total = []
    for i in range(max(a), min(b) + 1):
        acc = True
        for el in a:
            if i%el != 0:
                acc = False
                break
        for el in b:
            if el%i != 0:
                acc = False
                break
        if acc:
            total.append(i)
    return(len(total))
total = getTotalX(arr, brr)
print(str(total))