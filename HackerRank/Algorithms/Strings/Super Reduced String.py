s = 'aaabccddd'

def StringReduce(s):
    arr = [char for char in s]
    i = 0
    ln = len(arr)
    while i < ln-1:
        if arr[i] == arr[i+1]:
            del(arr[i:i+2])
            ln = len(arr)
            i = -1
        i += 1
    return(''.join(arr) or 'Empty String')

print(StringReduce(s))
