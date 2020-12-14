import re
num = '+.5486468'
startcon = bool(re.match(r'[+-.0-9]', num))
deccon = len(re.split(r'\.', num)) > 1
dotcon = bool(re.search(r'\.', num))
try:
    float(num)
    convcon = True
except:
    convcon = False
print(startcon & deccon & dotcon & convcon)

#import re
#for _ in range(input()):
#	print bool(re.match(r'^[-+]?[0-9]*\.[0-9]+$', raw_input()))