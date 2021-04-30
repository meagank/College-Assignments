######################################################################################################################
# Name: Meagan Kropp
# Date: April 4, 2020
# Description: creat sierpinski's triangle in python
######################################################################################################################
from Tkinter import *
from random import randint


# the 2D point class
class Point(object):
    def __init__(self, x = 0.0, y = 0.0):
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


# inherits from the Canvas class of Tkinter
class ChaosGame(Canvas):
    MIN_X = 2
    MAX_X = 594
    MIN_Y = 2
    MAX_Y = 514

    MID_X = (MIN_X + MAX_X)/2
    MID_Y = (MIN_Y + MAX_Y)/2

    

    def __init__(self, value):
            Canvas.__init__(self, value, bg = "white")
            self.pack(fill = BOTH, expand = 1)

    # set vertices
    def plotVertices(self, n):
        v1 = Point(self.MID_X, self.MIN_Y)
        v2 = Point(self.MIN_X, self.MAX_Y)
        v3 = Point(self.MAX_X, self.MAX_Y)
        self.create_oval(v1.x, v1.y, v1.x + 6, v1.y + 6, outline = "red", fill = "red")
        self.create_oval(v2.x, v2.y, v2.x + 6, v2.y + 6, outline = "red", fill = "red")
        self.create_oval(v3.x, v3.y, v3.x + 6, v3.y + 6, outline = "red", fill = "red")

        m1 = v2
        m1 = Point((v2.x + v1.x)/2, (v2.y + v1.y)/2)
        self.create_oval(m1.x, m1.y, m1.x + 2, m1.y + 2, outline = "black", fill = "black")

        for p in range(n):
            temp = randint(0,2)
            if (temp == 0):
                vt = v1
            elif (temp == 1):
                vt = v2
            else:
                vt = v3
                
            midpt = Point((m1.x + vt.x)/2, (m1.y + vt.y)/2)
            self.create_oval(midpt.x, midpt.y, midpt.x + 2, midpt.y + 2, outline = "black", fill = "black")
            m1 = midpt
        
        

######## MAIN PROGRAM ########
# size of the canvas
WIDTH = 600
HEIGHT = 520

NUM_POINTS = 50000
        

# create the window
window = Tk()
window.geometry("{}x{}".format(WIDTH, HEIGHT))
window.title("The Chaos Game")
# create the coordinate system as a Tkinter canvas inside the window
s = ChaosGame(window)
# plot some random points
s.plotVertices(NUM_POINTS)
# wait for the window to close
window.mainloop()
