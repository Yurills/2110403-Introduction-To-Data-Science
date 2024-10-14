class Complex:
 def __init__(self, a, b):
    self.a = a
    self.b = b
 # Constructor to initialize real (a) and imaginary (b) parts
 def __str__(self):
    if self.b < 0:
        return f'{self.a}{self.b}i'
    else:
        return f'{self.a}+{self.b}i'
 # Method to return a string representation of the complex number
 def __add__(self, rhs):
    self.a += rhs.a
    self.b += rhs.b
    return self
 # Method to add two complex numbers
 def __mul__(self, rhs):
    a = self.a*rhs.a - self.b*rhs.b
    b = self.a*rhs.b + self.b*rhs.a
    return Complex(a, b)
 # Method to multiply two complex numbers
 def __truediv__(self, rhs):
    a = (self.a*rhs.a + self.b*rhs.b)/(rhs.a**2 + rhs.b**2)
    b = (self.b*rhs.a - self.a*rhs.b)/(rhs.a**2 + rhs.b**2)
    return Complex(a, b)
 # Method to divide two complex numbers
#**Copy and paste your class with modified functions when submitting to the grader.

t, a, b, c, d = [int(x) for x in input().split()]
c1 = Complex(a,b)
c2 = Complex(c,d)
if t == 1 : print(c1)
elif t == 2 : print(c2)
elif t == 3 : print(c1+c2)
elif t == 4 : print(c1*c2)
else : print(c1/c2)