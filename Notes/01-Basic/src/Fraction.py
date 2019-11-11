# 1. how to define a class
# 2. show function definition in class and out of class
# 3. show main function
# 4. the meaning of self
#    When defining an instance method, 
#    the first parameter of the method should always be self 
#    (name convension from the python community).

#    The self in python represents or points the instance which it was called.

#    Explain it via Example (object called the function, the address of the 
#    instance will automatically passed to self)

class Fraction:

    def __init__(self,top,bottom):

        self.num = top
        self.den = bottom

    def show(self):
        print(self.num,"/",self.den)

    def __str__(self):
        return str(self.num)+"/"+str(self.den)

    def __add__(self,otherfraction):
        newnum = self.num*otherfraction.den + self.den*otherfraction.num
        newden = self.den * otherfraction.den
        common = gcd(newnum,newden)
        return Fraction(newnum//common,newden//common)

    def __eq__(self, other):
        firstnum = self.num * other.den
        secondnum = other.num * self.den
    
        return firstnum == secondnum

# calculate greatest common divisor
def gcd(m,n):
    while m%n != 0:
        oldm = m
        oldn = n

        m = oldn
        n = oldm%oldn
    return n

if __name__ == '__main__':
    x = Fraction(1,2)
    y = Fraction(2,3)

    x.show()
    y.show()

    print(x.__str__())

    z = x.__add__(y)
    z.show()

    result = x.__eq__(y)
    print(result)
