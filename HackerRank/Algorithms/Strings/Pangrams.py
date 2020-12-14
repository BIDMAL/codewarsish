inp = "We promptly judged antique ivory buckles for the next prize"
inp2 = "We promptly judged antique ivory buckles for the prize"

def IsPangram(s):
    alph = set('abcdefghijklmnopqrstuvwxyz')
    for char in s:
        if char.lower() in alph:
            alph.remove(char.lower())
    return(len(alph) == 0)

print('pangram' if IsPangram(inp2) else 'not pangram')