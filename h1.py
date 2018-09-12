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

def is_even(number = int):
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

def sum_of_1_to_n(n = int):
    """
    Calculates the sum of integers from 1 to given n
    n: positive integer
    Returns: integer
    """
    y = 0
    n = int (input("Choose a number:"))
    for x in range (1 + n):
        y = y + x
    print ( "This is the sum of all the numbers from 1 to your chosen number:", abs(y))

def miles_per_gallon(miles = float, gallons = float):
        """
         Calculates miles per gallons
         miles: positive float
         gallons: positive float
        """
        original_miles = float (input("Original miles travled before trip:"))
        driven_miles = float (input("Current number of miles on odometer:"))
        gallons = float (input("Gallons used:"))

        miles = driven_miles - original_miles
        print ("Total miles driven", abs(miles))
        mpg = miles / gallons
        print ("Miles per gallon", abs(mpg))

def sum_ten_random_1_10_interval( ):
    """
    Returns sum of  ten random integers in [1, 10]   interval
    """
    import random
    random_numbers =int
    sum = 0

    for x in range (10):
        random_numbers = random.randint(1,10)
        print (random_numbers)
        sum = random_numbers + sum
    print ("Here is the sum for all ten random numbers:", sum)

def average_odd_1_to_n(n = int):
    """
    Calculates the average of odd integers
    between 1 and given n
    n: positive integer 
    Returns: integer
    """
    from statistics import mean
    n = int (input("Choose a number:"))
    average = int
    average = mean (range(1, n + 1, 2))
    print ("Here is the average of all odd integers:", abs(average))





