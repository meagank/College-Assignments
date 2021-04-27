######################################################################################################################
# Name: Meagan Kropp
# Date: January 2, 2019
# Description: Create a vehicle class that has a year, make, and model and displays a year in the range
######################################################################################################################

# the vehicle class
# a vehicle has a year, make, and model

class Vehicle(object):
    
    def __init__(self, vehicle_make, vehicle_model):
        self.make = vehicle_make
        self.model = vehicle_model
        self.year = 2000

    #accessor for year
    @property
    def year(self):
        return self._year

    #mutator for year
    @year.setter
    def year(self, value):
        if (value > 1999 and value < 2020):
            self._year = value
        else:
            self._year

# ***DO NOT MODIFY OR REMOVE ANYTHING BELOW THIS POINT!***
# the main part of the program
v1 = Vehicle("Dodge", "Ram")
v2 = Vehicle("Honda", "Odyssey")
v3 = Vehicle("Toyota", "Highlander")
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)
print "v3={} {} {}".format(v3.year, v3.make, v3.model)
print

v1.year = 2010
v2.year = 2016
v3.year = 2008
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)
print "v3={} {} {}".format(v3.year, v3.make, v3.model)
print

v1.year = 1999
v2.model = "Civic"
v2.year = 2027
v3.year = 1980
print "v1={} {} {}".format(v1.year, v1.make, v1.model)
print "v2={} {} {}".format(v2.year, v2.make, v2.model)
print "v3={} {} {}".format(v3.year, v3.make, v3.model)

