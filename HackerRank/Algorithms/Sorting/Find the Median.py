inp = ['7',
       '0 1 2 4 6 5 3']
arr = list(map(int, inp[1].split()))
import statistics    
print(statistics.median(arr))