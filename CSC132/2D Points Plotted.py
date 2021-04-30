######################################################################################################################
# Name: Meagan Kropp
# Date: 3/26/2020
# Description: Plot some points in different colors
######################################################################################################################
from Tkinter import *
from random import randint


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

# the coordinate system class: (0,0) is in the top-left corner
# inherits from the Canvas class of Tkinter
class CoordinateSystem(Canvas):
    def __init__(self, value):
            Canvas.__init__(self, value, bg = "white")
            self.pack(fill = BOTH, expand = 1)
            self.point_color = value
            self.point_radius = value


    # accessor for point_color
    @property
    def point_color(self):
        return self._point_color

    # mutator for point_color
    @point_color.setter
    def point_color(self, value):
        self._point_color = value


    # accessor for point_radius
    @property
    def point_radius(self):
        return self._point_radius

    # mutator for point_radius
    @point_radius.setter
    def point_radius(self, value):
        self._point_radius = value
            

    # set points
    def plotPoints(self, n):
        for i in range(NUM_POINTS):
            x = randint(0, WIDTH - 1)
            y = randint(0, HEIGHT - 1)
            self.plot(x, y)

    def plot(self, x, y):
        pointColor = ["black", "red", "green", "blue", "cyan", "yellow", "magenta"]
        point_radius = 0
        point_color = pointColor[randint(0, len(pointColor)-1)]
        self.create_rectangle(x, y, x + (point_radius * 2), y + (point_radius * 2), outline = point_color, fill = point_color)

##########################################################
# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the default size of the canvas is 800x800
WIDTH = 800
HEIGHT = 800
# the number of points to plot
NUM_POINTS = 5000

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("2D Points...Plotted")
# create the coordinate system as a Tkinter canvas inside the window
s = CoordinateSystem(window)
# plot some random points
s.plotPoints(NUM_POINTS)
# wait for the window to close
window.mainloop()
