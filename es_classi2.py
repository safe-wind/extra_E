#class cylinder

class Cilynder:

    def __init__(self,height=1,radius=1,pi=3.14):

        self.height = height
        self.radius = radius
        self.pi = pi
    
    def volume(self):
        h = self.height
        r = self.radius
        p = self.pi
        return p*(r**2)*h

    def surface_area(self):
        h = self.height
        r = self.radius
        p = self.pi
        return (2*p*r*h)+(2*p*(r**2))
    
c = Cilynder(2,1)

print(f"V: {c.volume()}")

print(f"SF: {c.surface_area()}")