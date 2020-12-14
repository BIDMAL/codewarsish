#inp = ['6',
#       'aaabbb',
#       'ab',
#       'abc',
#       'mnop',
#       'xyyx',
#       'xaxbbbxx'] 
# 3 1 -1 2 0 1
inp = ['10',
       'hhpddlnnsjfoyxpciioigvjqzfbpllssuj',
       'xulkowreuowzxgnhmiqekxhzistdocbnyozmnqthhpievvlj',
       'dnqaurlplofnrtmh',
       'aujteqimwfkjoqodgqaxbrkrwykpmuimqtgulojjwtukjiqrasqejbvfbixnchzsahpnyayutsgecwvcqngzoehrmeeqlgknnb',
       'lbafwuoawkxydlfcbjjtxpzpchzrvbtievqbpedlqbktorypcjkzzkodrpvosqzxmpad',
       'drngbjuuhmwqwxrinxccsqxkpwygwcdbtriwaesjsobrntzaqbe',
       'ubulzt',
       'vxxzsqjqsnibgydzlyynqcrayvwjurfsqfrivayopgrxewwruvemzy',
       'xtnipeqhxvafqaggqoanvwkmthtfirwhmjrbphlmeluvoa',
       'gqdvlchavotcykafyjzbbgmnlajiqlnwctrnvznspiwquxxsiwuldizqkkaawpyyisnftdzklwagv']
#inp = ['1', 'dnqaurlplofnrtmh']
def anagram(s):
    ln = len(s)
    n = ln//2
    counter = 0
    if ln%2 == 0:
        lh = list(s[0:n])
        rh = list(s[n:])
        for i in range(n):
            if lh[i] not in rh:
                counter += 1
            else:
                rh.remove(lh[i])
    else:
        return -1
    return counter

for i in range(1, int(inp[0])+1):
    print(anagram(inp[i]))