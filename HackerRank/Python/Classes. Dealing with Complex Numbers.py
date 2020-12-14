import math
inp = ['2 1',
       '5 6']

class Complex(object):
    def __init__(self, real, imaginary):
        self.real = real
        self.imaginary = imaginary
    def __add__(self, no):
        return(Complex(self.real + no.real, self.imaginary + no.imaginary))
    def __sub__(self, no):
        return(Complex(self.real - no.real, self.imaginary - no.imaginary))
    def __mul__(self, no):
        return(Complex(self.real * no.real - self.imaginary * no.imaginary, self.real * no.imaginary + no.real * self.imaginary))
    def __truediv__(self, no):
        rNumer = self.real * no.real + self.imaginary * no.imaginary
        iNumer = self.imaginary * no.real - self.real * no.imaginary
        denom = no.real**2 + no.imaginary**2
        return(Complex(rNumer / denom, iNumer / denom))
    def mod(self):
        return(Complex(math.sqrt(self.real**2 + self.imaginary**2), 0))
    def __str__(self):
        if self.imaginary == 0:
            result = "%.2f+0.00i" % (self.real)
        elif self.real == 0:
            if self.imaginary >= 0:
                result = "0.00+%.2fi" % (self.imaginary)
            else:
                result = "0.00-%.2fi" % (abs(self.imaginary))
        elif self.imaginary > 0:
            result = "%.2f+%.2fi" % (self.real, self.imaginary)
        else:
            result = "%.2f-%.2fi" % (self.real, abs(self.imaginary))
        return result

if __name__ == '__main__':
    c = map(float, inp[0].split())
    d = map(float, inp[1].split())
    x = Complex(*c)
    y = Complex(*d)
    print(*map(str, [x+y, x-y, x*y, x/y, x.mod(), y.mod()]), sep='\n')


"""
7.00+7.00i
-3.00-5.00i
4.00+17.00i
0.26-0.11i
2.24+0.00i
7.81+0.00i
"""