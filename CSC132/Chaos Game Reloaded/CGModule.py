from math import sin,cos,pi


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

    def interpt(self, other, r):
        # make sure that the distance ratio is expressed from a
        # smaller component value to a larger one
        # first, the x-component
        rx = r
        if (self.x > other.x):
            rx = 1.0 - r
        # next, the y-component
        ry = r
        if (self.y > other.y):
            ry = 1.0 - r
            
        # calculate the new point's coordinates
        # the difference in the components (distance between the
        # points) is first scaled by the specified distance ratio
        # the minimum of the components is then added back in order
        # to obtain the coordinates in between the two points (and
        # not with respect to the origin)
        x = abs(self.x - other.x) * rx + min(self.x, other.x)
        y = abs(self.y - other.y) * ry + min(self.y, other.y)
        
        return Point(x, y)


class Fractal(object):
    def __init__(self, dimensions):

        self.dimensions = dimensions
        self.num_points = 50000
        self.r = 0.5

    @property
    def vertices(self):
        return self._vertices

    @vertices.setter
    def vertices(self, v):
        self._vertices = v


    def frac_x(self, r):
        return int((self.dimensions['MAX_X'] - self.dimensions['MIN_X']) * r) + self.dimensions['MIN_X']


    def frac_y(self, r):
        return int((self.dimensions['MAX_Y'] - self.dimensions['MIN_Y']) * r) + self.dimensions['MIN_Y']



class SierpinskiTriangle(Fractal):

    def __init__ (self, dimensions):
        Fractal.__init__(self, dimensions)

        self.num_points = 50000
        self.r = 0.5

        v1 = Point(dimensions['MID_X'],dimensions['MIN_Y'])
        v2 = Point(dimensions['MIN_X'], dimensions['MAX_Y'])
        v3 = Point(dimensions['MAX_X'], dimensions['MAX_Y'])
        self.vertices = [v1, v2, v3]


class SierpinskiCarpet(Fractal):

    def __init__ (self, dimensions):
        Fractal.__init__(self, dimensions)
        self.num_points = 100000
        self.r = 0.66

        v1 = Point(dimensions['MIN_X'],dimensions['MIN_Y'])
        v2 = Point(dimensions['MID_X'], dimensions['MIN_Y'])
        v3 = Point(dimensions['MAX_X'], dimensions['MIN_Y'])
        v4 = Point(dimensions['MIN_X'], dimensions['MID_Y'])
        v5 = Point(dimensions['MAX_X'], dimensions['MID_Y'])
        v6 = Point(dimensions['MIN_X'], dimensions['MAX_Y'])
        v7 = Point(dimensions['MID_X'], dimensions['MAX_Y'])
        v8 = Point(dimensions['MAX_X'], dimensions['MAX_Y'])
        self.vertices = [v1, v2, v3, v4, v5, v6, v7, v8]


class Pentagon(Fractal):

    def __init__ (self, dimensions):
        Fractal.__init__(self, dimensions)
        self.num_points = 50000
        self.r = 0.618
        

        v1 = Point(dimensions['MID_X'] + dimensions['MID_X'] * cos(2 * pi / 5 + 60), (self.frac_y(0.5375) + dimensions['MID_Y'] * sin(2 * pi / 5 + 60)))
        v2 = Point(dimensions['MID_X'] + dimensions['MID_X'] * cos(4 * pi / 5 + 60), (self.frac_y(0.5375) + dimensions['MID_Y'] * sin(4 * pi / 5 + 60)))
        v3 = Point(dimensions['MID_X'] + dimensions['MID_X'] * cos(6 * pi / 5 + 60), (self.frac_y(0.5375) + dimensions['MID_Y'] * sin(6 * pi / 5 + 60)))
        v4 = Point(dimensions['MID_X'] + dimensions['MID_X'] * cos(8 * pi / 5 + 60), (self.frac_y(0.5375) + dimensions['MID_Y'] * sin(8 * pi / 5 + 60)))
        v5 = Point(dimensions['MID_X'] + dimensions['MID_X'] * cos(10 * pi / 5 + 60), (self.frac_y(0.5375) + dimensions['MID_Y'] * sin(10 * pi / 5 + 60)))
        self.vertices = [v1, v2, v3, v4, v5]


class Hexagon(Fractal):

    def __init__ (self, dimensions):
        Fractal.__init__(self, dimensions)
        self.num_points = 50000
        self.r = 0.665
        

        v1 = Point(dimensions['MID_X'],dimensions['MIN_Y'])
        v2 = Point(dimensions['MIN_X'], self.frac_y(0.25))
        v3 = Point(dimensions['MAX_X'], self.frac_y(0.25))
        v4 = Point(dimensions['MIN_X'], self.frac_y(0.75))
        v5 = Point(dimensions['MAX_X'], self.frac_y(0.75))
        v6 = Point(dimensions['MID_X'], dimensions['MAX_Y'])
        self.vertices = [v1, v2, v3, v4, v5, v6]

class Octagon(Fractal):

    def __init__ (self, dimensions):
        Fractal.__init__(self, dimensions)
        self.num_points = 75000
        self.r = 0.705

        v1 = Point(self.frac_x(0.2925),dimensions['MIN_Y'])
        v2 = Point(self.frac_x(0.7075), dimensions['MIN_Y'])
        v3 = Point(dimensions['MIN_X'], self.frac_y(0.2925))
        v4 = Point(dimensions['MAX_X'], self.frac_y(0.2925))
        v5 = Point(dimensions['MIN_X'], self.frac_y(0.7075))
        v6 = Point(dimensions['MAX_X'], self.frac_y(0.7075))
        v7 = Point(self.frac_x(0.2925), dimensions['MAX_Y'])
        v8 = Point(self.frac_x(0.7075), dimensions['MAX_Y'])
        self.vertices = [v1, v2, v3, v4, v5, v6, v7, v8]

            
