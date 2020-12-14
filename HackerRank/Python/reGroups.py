import re
inp = '__init__'
m = re.search(r'([a-zA-Z0-9])\1', inp)
print(m.group(1) if m else -1)