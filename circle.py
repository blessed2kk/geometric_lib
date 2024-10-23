import math

def area(r):
    """
    Calculates the area of a circle given its radius.
    
    Formula:
    Area = π * r^2
    
    Parameters:
    r (float): The radius of the circle.
    
    Returns:
    float: The area of the circle.
    """
    return math.pi * r * r

def perimeter(r):
    """
    Calculates the circumference (perimeter) of a circle given its radius.
    
    Formula:
    Perimeter = 2 * π * r
    
    Parameters:
    r (float): The radius of the circle.
    
    Returns:
    float: The circumference of the circle.
    """
    return 2 * math.pi * r
