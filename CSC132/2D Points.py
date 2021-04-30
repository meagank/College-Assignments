######################################################################################################################
# Name: Meagan Kropp
# Date: March 17, 2020
# Description: Take some points and find the distance and midpoints between them.
######################################################################################################################
import math

# the 2D point class
class Point(object):
    def __init__(self, x = 0, y = 0):
        self.x = float(x)
        self.y = float(y)


    # accessor for x
    @property
    def x(self):
        return self._x

    # mutator for x
    @x.setter
    def x(self, value):
        self._x = value


    # accessor for y
    @property
    def y(self):
        return self._y

    # mutator for y
    @y.setter
    def y(self, value):
        self._y = value

    # distance function
    def dist(self, value):
        dx = self.x - value.x
        dy = self.y - value.y
        return math.sqrt((dx**2) + (dy**2))

    # midpoint function
    def midpt(self, value):
        mx = (self.x + value.x) / 2
        my = (self.y + value.y) / 2
        return Point(mx, my)

    def __str__(self):
        return "({},{})".format(self.x, self.y)
        
        
	

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# create some points
p1 = Point()
p2 = Point(3, 0)
p3 = Point(3, 4)
# display them
print "p1:", p1
print "p2:", p2
print "p3:", p3
# calculate and display some distances
print "distance from p1 to p2:", p1.dist(p2)
print "distance from p2 to p3:", p2.dist(p3)
print "distance from p1 to p3:", p1.dist(p3)
# calculate and display some midpoints
print "midpt of p1 and p2:", p1.midpt(p2)
print "midpt of p2 and p3:", p2.midpt(p3)
print "midpt of p1 and p3:", p1.midpt(p3)
# just a few more things...
p4 = p1.midpt(p3)
print "p4:", p4
print "distance from p4 to p1:", p4.dist(p1)
