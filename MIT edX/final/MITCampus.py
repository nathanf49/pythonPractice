### Do not change the Location or Campus classes. ###
### Location class is the same as in lecture.     ###
class Location(object):
    def __init__(self, x, y):
        #Initializes a coordinate with an x and y part
        self.x = x
        self.y = y

    def move(self, deltaX, deltaY):
        #moves the coordinate +x and +y ex: loc.move(2,0) is 2 to the right
        return Location(self.x + deltaX, self.y + deltaY)

    def getX(self): #returns only X part of coordinate
        return self.x

    def getY(self): #returns only y part of coordinate
        return self.y

    def dist_from(self, other): #finds hypotenuse distance between points
        xDist = self.x - other.x
        yDist = self.y - other.y
        return (xDist ** 2 + yDist ** 2) ** 0.5

    def __eq__(self, other):
        return (self.x == other.x and self.y == other.y)

    def __str__(self):
        return '<' + str(self.x) + ',' + str(self.y) + '>'


class Campus(object):
    def __init__(self, center_loc): #should take a location as center_loc
        self.center_loc = center_loc

    def __str__(self):
        return str(self.center_loc)


class MITCampus(Campus):
    """ A MITCampus is a Campus that contains tents """

    def __init__(self, center_loc, tent_loc=Location(0, 0)):
        """ Assumes center_loc and tent_loc are Location objects
        Initializes a new Campus centered at location center_loc
        with a tent at location tent_loc """
        if type(center_loc) != Location or type(tent_loc) != Location:
            raise ValueError
        Campus.__init__(self, center_loc)
        self.tents = [] #keeps track of tents
        self.add_tent(tent_loc)

    def add_tent(self, new_tent_loc):
        """ Assumes new_tent_loc is a Location
        Adds new_tent_loc to the campus only if the tent is at least 0.5 distance
        away from all other tents already there. Campus is unchanged otherwise.
        Returns True if it could add the tent, False otherwise. """
        if type(new_tent_loc) != Location:
            raise ValueError

        for element in self.tents: #checks distance and adds tent if there is enough distance
            if new_tent_loc.dist_from(element) < 0.5:
                return False
        self.tents.append(new_tent_loc)
        return True

    def remove_tent(self, tent_loc):
        """ Assumes tent_loc is a Location
        Removes tent_loc from the campus.
        Raises a ValueError if there is not a tent at tent_loc.
        Does not return anything """
        if type(tent_loc) != Location:
            raise ValueError
        if tent_loc in self.tents: #checks if tent Location is in the tents list
            self.tents.remove(tent_loc)
        else:
            raise ValueError

    def get_tents(self):
        """ Returns a list of all tents on the campus. The list should contain
        the string representation of the Location of a tent. The list should
        be sorted by the x coordinate of the location. """

        for tent in range(len(self.tents) - 1): #selection sort
            if self.tents[tent].getX() > self.tents[tent + 1].getX():
                temp = self.tents[tent + 1]
                self.tents[tent + 1] = self.tents[tent]
                self.tents[tent] = temp

        tentLocations = []
        for location in self.tents: #converts to string
            tentLocations.append(str(location))

        return tentLocations




x = MITCampus(Location(0,0))
x.add_tent((Location(5,5)))
x.add_tent(Location(1,1))

c = MITCampus(Location(1,2)) #then executing the following sequence of commands:

c.add_tent(Location(2,3)) #should return True
c.add_tent(Location(1,2)) #should return True
c.add_tent(Location(0,0)) #should return False
c.add_tent(Location(2,3)) #should return False
c.get_tents() #should return ['<0,0>', '<1,2>', '<2,3>']