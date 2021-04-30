######################################################################################################################
# Name: Meagan Kropp
# Date: May 14, 2020
# Description: creat sierpinski's triangle in python
######################################################################################################################
from Tkinter import *
from CGModule import *
from random import randint

class ChaosGame(Canvas):

    def __init__ (self, value):
        Canvas.__init__(self, value, bg = "white")
        self.pack(fill = BOTH, expand = 1)

        self.dimensions = {}

        self.dimensions["WIDTH"] = WIDTH
        self.dimensions["HEIGHT"] = HEIGHT
        self.dimensions["MIN_X"] = 5
        self.dimensions["MAX_X"] = self.dimensions["WIDTH"] - 5
        self.dimensions["MIN_Y"] = 5
        self.dimensions["MAX_Y"] = self.dimensions["HEIGHT"] - 5
        self.dimensions["MID_X"] = (self.dimensions["MIN_X"] + self.dimensions["MAX_X"])/2
        self.dimensions["MID_Y"] = (self.dimensions["MIN_Y"] + self.dimensions["MAX_Y"])/2

        self.vertex_radius = 6
        self.vertex_color = "red"
        self.point_radius = 1
        self.point_color = "black"

    def make(self, f):
        if (f == "SierpinskiTriangle"):
            frac = SierpinskiTriangle(self.dimensions)
        elif (f == "SierpinskiCarpet"):
            frac = SierpinskiCarpet(self.dimensions)
        elif (f == "Pentagon"):
            frac = Pentagon(self.dimensions)
        elif (f == "Hexagon"):
            frac = Hexagon(self.dimensions)
        elif (f == "Octagon"):
            frac = Octagon(self.dimensions)


        print "Generating.... {}".format(f)
        for v in frac.vertices:
            self.plot_point(v, self.vertex_color, self.vertex_radius)


        temp = Point(300, 260)
        for n in range(frac.num_points):
            tmp2 = randint(0, len(frac.vertices) - 1)
            temp = Point.interpt(temp, frac.vertices[tmp2], frac.r)
            self.plot_point(temp, "black", 1)

            
    def plot_point(self, point, ptColor, ptRadius):
        self.create_oval(point.x, point.y, point.x + ptRadius * 2, point.y + ptRadius * 2, outline = ptColor, fill = ptColor)
    


######## MAIN PROGRAM ########
# the default size of the canvas is 600x520
WIDTH = 600
HEIGHT = 520


# the implemented fractals
FRACTALS = [ "SierpinskiTriangle", "SierpinskiCarpet", "Pentagon", "Hexagon", "Octagon"]

# create the fractals in individual (sequential) windows
for f in FRACTALS:
    window = Tk()
    window.geometry("{}x{}".format(WIDTH, HEIGHT))
    window.title("The Chaos Game...Reloaded")
    # create the game as a Tkinter canvas inside the window
    s = ChaosGame(window)
    # make the current fractal
    s.make(f)
    # wait for the window to close
    window.mainloop()
