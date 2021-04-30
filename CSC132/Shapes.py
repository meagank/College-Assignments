######################################################################################################################
# Name: Meagan Kropp
# Date: 4/15/2020
# Description: use inheritance to print out astericks in specific shapes
######################################################################################################################
class Shape(object):
    def __init__(self, w, h):
        self.width = w
        self.height = h


    # accessor for width
    @property
    def width(self):
        return self._width

    # mutator for width
    @width.setter
    def width(self, value):
        if (value > 0):
            self._width = value
        else:
            self._width = 1

    # accessor for height
    @property
    def height(self):
        return self._height

    # mutator for height
    @height.setter
    def height(self, value):
        if (value > 0):
            self._height = value
        else:
            self._height = 1

    def __str__(self):
        temp = ""
        for i in range(self.height):
            temp += "* " * self.width + "\n"
        return temp


class Rectangle(Shape):
    def __init__(self, w, h):
        Shape.__init__(self, w, h)


class Square(Shape):
    def __init__(self, w):
        Shape.__init__(self, w, w)


class Triangle(Shape):
    def __init__(self, w):
        Shape.__init__(self, w, w)

    def __str__(self):
        temp = ""
        for i in range(self.height):
            temp += "* " * (self.height - i) + "\n"
        return temp

class Parallelogram(Shape):
    def __init__(self, w, h):
        Shape.__init__(self, w, h)


    def __str__(self):
        temp = ""
        for i in range(self.height - 1, -1, -1):
            temp += (i * " ") + ("* " * self.width) + "\n"
        return temp




##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create and display several shapes
r1 = Rectangle(12, 4)
print r1
s1 = Square(6)
print s1
t1 = Triangle(7)
print t1
p1 = Parallelogram(10, 3)
print p1
r2 = Rectangle(0, 0)
print r2
p1.width = 2
p1.width = -1
p1.height = 2
print p1




    

