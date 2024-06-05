import math

class polygon:
    def __init__(self, side, length):
        self.side = side
        self.length = length

    def area (self):
        return round ((self.length * self.side ** 2) / (4 * math.tan(math.pi / self.length)), 2)
    
    def perimeter(self):
        return round (self.length * self.side, 2)


class circle:
    def __init__(self, radius):
        self.radius = radius

    def area (self):
        return round (math.pi * self.radius ** 2, 2)
    
    def perimeter(self):
        return round (2 * math.pi * self.radius, 2)


if __name__ == "__main__":
    side = int(input('Choose how much sides figure have. For circle type 0: '))
    if side >= 3:
        poly = polygon(side, float(input('Type lengths of sides in cm: ')))
        print (f"Area: {poly.area()}. Perimeter: {poly.perimeter()}.")
    elif side == 0:
        circ = circle(float(input('Type radius in cm: ')))
        print (f"Area: {circ.area()}. Perimeter: {circ.perimeter()}.")
    else:
        print ('Error: Wrong input')