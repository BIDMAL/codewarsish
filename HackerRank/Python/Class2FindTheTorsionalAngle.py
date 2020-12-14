import math
import numpy as np

class Points(object):
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
    def __sub__(self, no):
        return(Points(self.x - no.x, self.y - no.y, self.z - no.z))
    def dot(self, no):
        return(self.x * no.x + self.y * no.y + self.z * no.z)
    def cross(self, no):
        return(Points(self.y * no.z - self.z * no.y,
                      self.z * no.x - self.x * no.z,
                      self.x * no.y - self.y * no.x))
    def absolute(self):
        return pow((self.x ** 2 + self.y ** 2 + self.z ** 2), 0.5)

a = [0, 4, 5]
va = np.array(a)
pa = Points(*a)
b = [1, 7, 6]
vb = np.array(b)
pb = Points(*b)

#print(va - vb)
#print((pa - pb).x, (pa - pb).y, (pa - pb).z)

print(np.dot(va,vb))
print(pa.dot(pb))