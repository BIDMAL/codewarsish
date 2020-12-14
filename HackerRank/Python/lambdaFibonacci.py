cube = lambda x: x**3 

def fibonacci(n):
    l = [0, 1]
    for _ in range(2,n):
        l.append(l[-2]+l[-1]) 
    return(l[:n])

n = int(3)

print(list(map(cube, fibonacci(n))))
