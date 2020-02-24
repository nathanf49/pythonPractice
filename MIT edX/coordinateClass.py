class coordinate:
    def __init__(self, x, y):  # assigns inputs for each instance of class
        if (type(x) is not int and type(x) is not float) or (type(y) is not int and type(y) is not float):
            raise TypeError("Coordinates must be of type int or type float")
        self.x = x
        self.y = y

    def __str__(self):  # changes how the string is returned (for print statements mostly)
        return "<" + str(self.x) + "," + str(self.y) + ">"

    def distanceFromOrigin(self):
        return ((self.x ** 2) + (self.y ** 2)) ** 0.5

    def distanceFromPoint(self, x, y):
        return (((self.x - x) ** 2) + ((self.y - y) ** 2)) ** 0.5

    def distanceBetweenPoints(self, otherCoordinate):
        if type(otherCoordinate) is not coordinate:
            raise TypeError("You must input another coordinate to find the difference between two coordinates")
        return (((self.x - otherCoordinate.x) ** 2) + ((self.y - otherCoordinate.y) ** 2)) ** 0.5
