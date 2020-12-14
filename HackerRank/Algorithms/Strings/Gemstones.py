inp = ['3',
       'abcdde',
       'baccd',
       'eeabg']

def CountGemstones(arr):
    mnrs = [set(rock) for rock in arr]
    return(len(mnrs[0].intersection(*mnrs)))
    

rocks = []
for i in range(1, int(inp[0])+1):
    rocks.append(inp[i])

print(CountGemstones(rocks))