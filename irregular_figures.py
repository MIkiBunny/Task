import math


def get_correct_type(prompt=""):
    """
    Check if typed text is a number and prompt again if not.
    
    prompt: Optional prompt to display to the user.

    return: The int value entered by the user.
    """
    while True:
        try:
            value = int(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def get_numeric_coord(prompt=""):
    """
    Check if typed text is a number and prompt again if not.
    
    prompt: Optional prompt to display to the user.

    return: The float value entered by the user.
    """
    while True:
        try:
            value = float(input(prompt))
            return value
        except ValueError:
            print("Please enter a valid number.")


def calculate_polygon (side, coorx,coory):
    """
    Calculate area and perimeter of any regular polygon
    
    side: number of sides
    coorx: Array of x coordinates of polygon 
    coory: Array of y coordinates of polygon 

    return: area and perimeter of the polygon.
    """
    area  = 0
    perimeter = 0
    for i in range(side):
        nexti = (i + 1) % side  
        area += coorx[i] * coory[nexti] - coory[i] * coorx[nexti]
        perimeter += abs((coorx[i] - coorx[nexti]) ** 2 + (coory[i] - coory[nexti]) ** 2)
    area = round (abs(area)/2, 2)
    perimeter = round (abs(math.sqrt(perimeter)), 2)
    return area, perimeter


def calculate_circle (coorx, coory):
    """
    Calculate area and perimeter of circle.
    
    coorx: Array of x coordinates of circle.
    coory: Array of y coordinates of circle.

    return: area and perimeter of the circle.
    """
    radius = abs(math.sqrt((coorx[0] - coorx[1]) ** 2 + (coory[0] - coory[1]) ** 2))
    perimeter = round (2 * math.pi * radius, 2)
    area = round (math.pi * radius ** 2, 2)
    return area, perimeter


def main():
    """
    Main function to calculate area and perimeter based on user input
    """
    coorx = [] #array for coordinate x
    coory = [] #array for coordinate y
    side = get_correct_type('Choose how much sides figure have. For circle type 0: ')
    if side == 0:
        coorx.append (get_numeric_coord('Type x coordinate for centre: '))
        coory.append (get_numeric_coord('Type y coordinate for centre: '))
        coorx.append (get_numeric_coord('Type x coordinate for point on circumference: '))
        coory.append (get_numeric_coord('Type y coordinate for point on circumference: '))
        area, perimeter = calculate_circle(coorx, coory)
        print ('Area:', area, '. Perimeter: ', perimeter, '.')
    elif side >= 3:
        for i in range(side):
            coorx.append (get_numeric_coord('Type x coordinate for side {}: '.format(i)))
            coory.append (get_numeric_coord('Type y coordinate for side {}: '.format(i)))
        area, perimeter = calculate_polygon(side, coorx, coory)
        print ('Area:', area, '. Perimeter: ', perimeter, '.')


if __name__ == "__main__":
    main()