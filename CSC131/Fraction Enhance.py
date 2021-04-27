######################################################################################################################
# Name: Meagan Kropp
# Date: January 8, 2019
# Description: Implement a fraction class that allows arithmetic operators to be used on the fractions.
######################################################################################################################

# the fraction class
class Fraction(object):
    # constructor
    def __init__(self, num = 0, den = 1):
        self.num = num
        # if denominator is zero, change it to one
        if (den == 0):
            den = 1
        self.den = den

    # accessor for the numerator
    @property
    def num(self):
        return self._num

    # mutator for the numerator
    @num.setter
    def num(self, value):
        self._num = value

    # accessor for the denominator
    @property
    def den(self):
        return self._den

    # mutator for the denominator
    @den.setter
    def den(self, value):
        # ignore if the denominator is zero
        if (value != 0):
            self._den = value
    # numeric representation of fractions
    def getReal(self):
        return float(self.num) / self.den

    # reduce a fraction
    def reduce(self):
        # assume the greatest common divisor (gcd) is 1
        gcd = 1
        # find the minimum of the numerator and the denominator
        minimum = min(abs(self.num), abs(self.den))

        # find common divisors
        for i in range(2, minimum + 1):
            # check if num and den are evenly divisible by i
            if(self.num % i == 0 and self.den % i == 0):
                # update gcd
                gcd = i
        # divide numerator and denominator by the gcd
        self.num /= gcd
        self.den /= gcd

        # if the numerator is zero, set the denominator to one
        if (self.num == 0):
            self.den = 1


    # add two fractions
    def __add__(self, other):
        num = (self.den * other.num) + (other.den * self.num)
        den = (self.den * other.den)
        sum = Fraction(num, den)

        return sum

    # subtract two fractions
    def __sub__(self, other):
        num = (self.den * other.num) - (other.den * self.num)
        den = (self.den * other.den)
        difference = Fraction(num, den)

        return difference

    # multiply two fractions
    def __mul__(self, other):
        num = (self.num * other.num)
        den = (self.den * other.den)
        product = Fraction(num, den)

        return product


    # multiply two fractions
    def __div__(self, other):
        num = (self.num * other.den)
        den = (self.den * other.num)
        quotient = Fraction(num, den)

        return quotient

    # return the string representation of the fraction
    def __str__(self):
        self.reduce()
        return "{}/{} ({})".format(self.num, self.den, self.getReal())


# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
# create some fractions
f1 = Fraction()
f2 = Fraction(5, 8)
f3 = Fraction(3, 4)
f4 = Fraction(1, 0)

# display them
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

# play around
f3.num = 5
f3.den = 8
f1 = f2 + f3
f4.den = 88
f2 = f1 - f1
f3 = f1 * f1
f4 = f4 / f3

# display them again
print
print "f1:", f1
print "f2:", f2
print "f3:", f3
print "f4:", f4

