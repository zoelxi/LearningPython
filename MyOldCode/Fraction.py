import math

class Fraction:
    '''represents fractions'''

    def __init__(self,num,denom):
        '''Fraction(num,denom) -> Fraction
        creates the fraction object representing num/denom'''
        if denom == 0: # raise an error if the denominator is zero
            raise ZeroDivisionError
        self.num = num
        self.denom = denom

    def __str__(self):
        '''str(Fraction) -> str
        returns string representing fraction in lowest terms with a positive denominator'''
        gcd = math.gcd(self.num,self.denom)
        # represents fraction in lowest terms
        self.num = self.num//gcd
        self.denom = self.denom//gcd
        # creates positive denominator
        if self.denom < 0:
            self.denom = self.denom*(-1)
            self.num = self.num*(-1)
        return str(self.num) + '/' + str(self.denom)

    def __float__(self):
        '''float(Fraction) -> float
        returns float equal to fraction'''
        return self.num/self.denom

    def __add__(self,other):
        '''add(Fraction,Fraction) -> Fraction
        returns sum of two fractions'''
        lcm = (self.denom*other.denom)//math.gcd(self.denom,other.denom)
        # creates common denominator
        denom = lcm 
        num = self.num*(lcm//self.denom) + other.num*(lcm//other.denom)
        return Fraction(num,denom)
        
    def __sub__(self,other):
        '''sub(Fraction,Fraction) -> Fraction
        returns difference between two fractions'''
        lcm = (self.denom*other.denom)//math.gcd(self.denom,other.denom)
        # creates common denominator
        denom = lcm
        num = self.num*(lcm//self.denom) - other.num*(lcm//other.denom)
        return Fraction(num,denom)

    def __mul__(self,other):
        '''mul(Fraction,Fraction) -> Fraction
        returns product of two fractions'''
        num = self.num*other.num
        denom = self.denom*other.denom
        return Fraction(num,denom)

    def __truediv__(self,other):
        '''truediv(Fraction,Fraction) -> Fraction
        returns quotient of two fractions'''
        # multiplies fraction by reciprocal of other fraction
        num = self.num*other.denom
        denom = self.denom*other.num
        return Fraction(num,denom)

    def __eq__(self,other):
        '''eq(Fraction,Fraction) -> bool
        returns True if two fractions are equal and False if not'''
        if self.num == other.num and self.denom == other.denom: # checks if numerators and denominators are equal
            return True
        return False

# examples
p = Fraction(3,6)
print(p)  # should print 1/2
q = Fraction(10,-60)
print(q)  # should print -1/6
r = Fraction(-24,-48)
print(r)  # should also print 1/2
x = float(p)
print(x)  # should print 0.5
### if overloading using special methods
print(p+q)  # should print 1/3
print(p-q)  # should print 2/3
print(p-p)  # should print 0/1
print(p*q)  # should print -1/12 
print(p/q)  # should print -3/1
print(p==r) # should print True
print(p==q) # should print False
