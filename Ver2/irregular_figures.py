import math


class polygon:

    count  = 0 #needed to be able make +=

    def __init__(self, side, x, y):
        self.side = side
        self.x = x
        self.y = y

    def area(self):
        for i in range(side):
            nexti = (i + 1) % side  
            self.count += self.x[i] * self.y[nexti] - self.y[i] * self.x[nexti]
        return round (abs(self.count)/2, 2)
    
    def perimeter(self):
        for i in range(side):
            nexti = (i + 1) % side 
            self.count += math.sqrt((self.x[i] - self.x[nexti]) ** 2 + (self.y[i] - self.y[nexti]) ** 2)
        return round (abs(self.count))

class circle:

    def __init__(self, x, y) -> None:
        self.x = x
        self.y = y
        self.radius = abs(math.sqrt((x[0] - x[1]) ** 2 + (y[0] - y[1]) ** 2))

    def area(self):
        return round (math.pi * self.radius ** 2, 2)
    
    def perimeter(self):
        return round (2 * math.pi * self.radius, 2)


if __name__ == "__main__":
    x = [] #array for coordinate x
    y = [] #array for coordinate y
    side = int(input('Choose how much sides figure have. For circle type 0: '))
    if side == 0:
        for i in range(2):
            x.append (float(input('Type x coordinate: ')))
            y.append (float(input('Type y coordinate: ')))
        circ = circle(x, y)
        print (f"Area: {circ.area()}. Perimeter: {circ.perimeter()}.")
    elif side >= 3:
        for i in range(side):
            x.append (float(input(f"Type x coordinate for side {i+1}: ")))
            y.append (float(input(f"Type y coordinate for side {i+1}: ")))
        poly = polygon(side, x, y)
        print (f"Area: {poly.area()}. Perimeter: {poly.perimeter()}.")
    else:
        print ('Error: Wrong input')