import math

class Polygon:
    """
    A class used to represent a Polygon.

    Attributes

    side : int
        Number of sides of the polygon.
    x : list
        List of x-coordinates of the vertices.
    y : list
        List of y-coordinates of the vertices.
    area_value : float
        Calculated area of the polygon.
    perimeter_value : float
        Calculated perimeter of the polygon.

    Methods

    calculate_area():
        Calculates and returns the area of the polygon.
    calculate_perimeter():
        Calculates and returns the perimeter of the polygon.
    """

    def __init__(self, side: int, x, y):
        self.side = side
        self.x = x
        self.y = y
        self.area_value = self.calculate_area()
        self.perimeter_value = self.calculate_perimeter()

    def calculate_area(self) -> float:
        area = 0
        for i in range(self.side):
            nexti = (i + 1) % self.side
            area += self.x[i] * self.y[nexti] - self.y[i] * self.x[nexti]
        area = round(abs(area) / 2, 2)
        return area

    def calculate_perimeter(self) -> float:
        perimeter = 0
        for i in range(self.side):
            nexti = (i + 1) % self.side
            perimeter += math.sqrt((self.x[i] - self.x[nexti])**2 + (self.y[i] - self.y[nexti])**2)
        perimeter = round(perimeter, 2)
        return perimeter

class Circle:
    """
    A class used to represent a Circle.

    Attributes

    x : list
        List of x-coordinates for two points (center and a point on the circumference).
    y : list
        List of y-coordinates for two points (center and a point on the circumference).
    radius : float
        Calculated radius of the circle.
    area_value : float
        Calculated area of the circle.
    perimeter_value : float
        Calculated perimeter of the circle.

    Methods

    calculate_area():
        Calculates and returns the area of the circle.
    calculate_perimeter():
        Calculates and returns the perimeter of the circle.
    """
    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.radius = abs(math.sqrt((x[0] - x[1])**2 + (y[0] - y[1])**2))
        self.area_value = self.calculate_area()
        self.perimeter_value = self.calculate_perimeter()

    def calculate_area(self) -> float:
        area = round(math.pi * self.radius**2, 2)
        return area

    def calculate_perimeter(self) -> float:
        perimeter = round(2 * math.pi * self.radius, 2)
        return perimeter

def get_correct_type(prompt: str, float_type=False) -> float:
    """
    Prompts the user for input and returns the correct type (float or int).

    Parameters

    prompt : str
        The input prompt to be displayed.
    float_type : bool, optional
        Whether the expected input is a float (default is False).

    Returns

    float
        The input value converted to the correct type.
    """
    while True:
        try:
            value = float(input(prompt)) if float_type else int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")

def main():
    x = []
    y = []
    side = get_correct_type('Choose how many sides the figure has. For a circle type 0: ', float_type=False)
    if side == 0:
        for i in range(2):
            x.append(get_correct_type('Type x coordinate: ', float_type=True))
            y.append(get_correct_type('Type y coordinate: ', float_type=True))
        circ = Circle(x, y)
        print(f"Area: {circ.area_value}. Perimeter: {circ.perimeter_value}.")
    elif side >= 3:
        for i in range(side):
            x.append(get_correct_type(f"Type x coordinate for vertex {i+1}: ", float_type=True))
            y.append(get_correct_type(f"Type y coordinate for vertex {i+1}: ", float_type=True))
        poly = Polygon(side, x, y)
        print(f"Area: {poly.area_value}. Perimeter: {poly.perimeter_value}.")
    else:
        print('Error: Wrong input')

if __name__ == "__main__":
    main()