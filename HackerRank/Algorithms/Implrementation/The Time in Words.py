inp = '7 36'
h, m = map(int, inp.split())

def timeToWords(h, m):
    digits = ['one', 'two', 'three', 'four', 'five', 'six', 
              'seven', 'eight', 'nine', 'ten', 'eleven', 
              'twelve', 'thirteen', 'fourteen', 'fifteen', 
              'sixteen', 'seventeen', 'eighteen', 'nineteen']
    if m <=30:
        wh = digits[h-1]
    else:
        wh = digits[h%12]
    
    if m == 0:
        return f"{wh} o' clock"
    elif m == 1:
        return f"one minute past {wh}"
    elif m == 15:
        return f"quarter past {wh}"
    elif m == 30:
        return f"half past {wh}"
    elif m == 45:
        return f"quarter to {wh}"
    elif m == 20:
        return f"twenty minutes past {wh}"
    elif m == 40:
        return f"twenty minutes to {wh}"
    elif m < 20:
        return f"{digits[m-1]} minutes past {wh}"
    elif m > 20 and m < 30:
        return f"twenty {digits[(m-1)%20]} minutes past {wh}"
    elif m > 30 and m < 40:
        return f"twenty {digits[(59-m)%20]} minutes to {wh}"
    elif m > 40:
        return f"{digits[59-m]} minutes to {wh}"
    return digits[1]
    
print(timeToWords(h, m))