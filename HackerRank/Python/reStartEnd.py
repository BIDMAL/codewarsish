import re

for m in re.finditer(r'(aa)','aaadaa'):
    print((m.start(), m.end()) if m else (-1, -1))