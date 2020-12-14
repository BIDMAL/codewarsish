import collections
import operator
s = 'aabbbccde'
chars = collections.Counter(s).items()

for char, n in sorted(chars, key=lambda c: (-c[1], c[0]))[:3]:
    print(char, n)