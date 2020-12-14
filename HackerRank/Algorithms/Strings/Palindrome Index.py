import math
#inp = ['4',                 #3 0 -1 1
#       'aaab',
#       'baa',
#       'aaa',
#       'quyjjdcgsvvsgcdjjyq']
inp = ['1',
       'hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh']
#inp = ['10',
#       'quyjjdcgsvvsgcdjjyq',
#       'hgygsvlfwcwnswtuhmyaljkqlqjjqlqkjlaymhutwsnwcflvsgygh',
#       'fgnfnidynhxebxxxfmxixhsruldhsaobhlcggchboashdlurshxixmfxxxbexhnydinfngf',
#       'bsyhvwfuesumsehmytqioswvpcbxyolapfywdxeacyuruybhbwxjmrrmjxwbhbyuruycaexdwyfpaloyxbcpwsoiqtymhesmuseufwvhysb',
#       'fvyqxqxynewuebtcuqdwyetyqqisappmunmnldmkttkmdlnmnumppasiqyteywdquctbeuwenyxqxqyvf',
#       'mmbiefhflbeckaecprwfgmqlydfroxrblulpasumubqhhbvlqpixvvxipqlvbhqbumusaplulbrxorfdylqmgfwrpceakceblfhfeibmm',
#       'tpqknkmbgasitnwqrqasvolmevkasccsakvemlosaqrqwntisagbmknkqpt',
#       'lhrxvssvxrhl',
#       'prcoitfiptvcxrvoalqmfpnqyhrubxspplrftomfehbbhefmotfrlppsxburhyqnpfmqlaorxcvtpiftiocrp',
#       'kjowoemiduaaxasnqghxbxkiccikxbxhgqnsaxaaudimeowojk']

def palindromeIndex(s):
    ln = len(s)
    n = ln // 2
    nr = math.ceil(ln/2)
    l = s[:n+1]
    r = s[:nr-2:-1]
    ind = -1
    res = l ==r
    if not res:
        for i in range(n):
            if l[i] != r[i]:
                if l[i:n] == r[i+1:]:
                    ind = ln - 1 - i
                    break
                else:
                    ind = i
                    break
    return ind

for i in range(1, int(inp[0]) + 1):
    print(palindromeIndex(list(inp[i])))