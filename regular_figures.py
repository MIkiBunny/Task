import math


def calculate_polygon (length,side):
    """
    Calculate area and perimeter of any regular polygon
    
    length: The length of all sides of the polygon.
    side: The number of sides.
    
    return: The area and perimeter of the polygon.
    """
    perimeter = round (length*side, 2)
    area = round ((length * side ** 2) / (4 * math.tan(math.pi / length)), 2)
    return area, perimeter


def calculate_circle (radius):
    """
    Calculate area and perimeter of circle
    
    radius: The radius of the circle.
    
    return: The area and perimeter of the circle.
    """
    perimeter = round (2 * math.pi * radius, 2)
    area = round (math.pi * radius ** 2, 2)
    return area, perimeter


def main():
    """
    Main function to calculate area and perimeter based on user input
    """
    side = int(input('Choose how much sides figure have. For circle type 0: '))
    if side >= 3:
        length = float(input('Type lengths of sides in cm: '))
        area, perimeter = calculate_polygon(length, side)
        print ('Area:', area, '. Perimeter: ', perimeter, '.')
    elif side == 0:
        length = float(input('Type radius in cm: '))
        area, perimeter = calculate_circle(length)
        print ('Area:', area, '. Perimeter: ', perimeter, '.')
    else:
        print ('Error: Wrong input')


if __name__ == "__main__":
    main()