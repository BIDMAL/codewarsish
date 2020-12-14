import math
inp = ['4',
       '1',
       '2',
       '7',
       '169']

def is_smart_number(num):
    val = int(math.sqrt(num))
    if num / val == val:
        return True
    return False

for i in range(int(inp[0])):
    num = int(inp[1+i])
    ans = is_smart_number(num)
    if ans:
        print("YES")
    else:
        print("NO")