# Fill in the Line class methods to accept coordinates as a 
# pair of tuples and return the slope and distance of the 
# line.

class Line:

    def __init__(self, coord1:tuple, coord2:tuple):
        
        self.coord1 = coord1
        self.coord2 = coord2

    def slope(self):

        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return (y2-y1)/(x2-x1)
    
    def distance(self):

        x1,y1 = self.coord1
        x2,y2 = self.coord2
        return ((x2-x1)**2)+((y2-y1)**2)*(1/2)

coord1 = (3,2)
coord2 = (8,10)


li = Line(coord1,coord2)

print(li.distance())

print(li.slope())