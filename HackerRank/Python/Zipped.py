import numpy as np
l = ['89 90 78 93 80',
     '90 91 85 88 86',
     '91 92 83 89 90.5']

nStud, nSub = 5, 3
subs = []
for i in range(nSub):
    subs.append(list(map(float, l[i].split())))
subs = zip(*subs)
subsum = list(map(sum, subs))
av=[]
for s in subsum:
     av.append(s/nSub)
for v in av:
     print('%0.1f' % v)

# n, x = map(int, input().split()) 
# 
# sheet = []
# for _ in range(x):
#     sheet.append( map(float, input().split()) ) 
# 
# for i in zip(*sheet): 
#     print( sum(i)/len(i) )