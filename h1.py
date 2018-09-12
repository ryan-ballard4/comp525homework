"""
Comp 525
h1.py
Ryan Ballard
9/12/2018
"""

def circle_area(radius = float):
    """
    Calculates the area of a circle with given radius.
    radius: non-negative float
    Returns: float
    """
    import math
    radius = float (input("What is the radius of the circle?"))
    area = float
    area = (math.pi *(radius * radius))
    print("The area is", abs(area))

def is_even(number):
    """
    Checks if number is even
    number: integer
    Returns: True if number is even, False otherwise
    """
number = int (input("Choose a number:"))
if number % 2 == 0:
    print ("True")
else:
    print ("False")