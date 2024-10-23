def area(a, h):
    """
    Calculates the area of a triangle given its base and height.
    
    Formula:
    Area = (base * height) / 2
    
    Parameters:
    a (float): The length of the base of the triangle.
    h (float): The height of the triangle.
    
    Returns:
    float: The area of the triangle.
    """
    return a * h / 2


def perimeter(a, b, c):
    """
    Calculates the perimeter of a triangle given the lengths of its three sides.
    
    Formula:
    Perimeter = side1 + side2 + side3
    
    Parameters:
    a (float): The length of the first side of the triangle.
    b (float): The length of the second side of the triangle.
    c (float): The length of the third side of the triangle.
    
    Returns:
    float: The perimeter of the triangle.
    """
    return a + b + c
