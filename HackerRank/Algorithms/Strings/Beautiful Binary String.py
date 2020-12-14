inp = ['10',
       '0100101010']

import re

def beautifulBinaryString(b):
    return(len(re.findall(r'010', b)))

print(beautifulBinaryString(inp[1]))
