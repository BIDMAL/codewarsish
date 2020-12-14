n = 3
def viralAdvertising(n):
    liked = 2
    new = 5
    for _ in range(2,n+1):
        new = (new // 2) * 3
        liked += new // 2
    return(liked)

print(viralAdvertising(n))