class Complex():
    def __init__(self, r, i):
        self.r = r
        self.i = i
    def __repr__(self):
        if self.i < 0:
            return "{} - i{}".format(self.r, abs(self.i))
        else:    
            return "{} + i{}".format(self.r, self.i)
    def __add__(self, other):
        #print( "{} + i{}".format(self.r + other.r , self.i + other.i))
        return Complex(self.r + other.r, self.i + other.i)
        
c = Complex(5,-7)
d = Complex(3,7)
#e = Complex(-3,-7)
e = c + d
print(c)
print(d)
print(e)
print (c + d + e)