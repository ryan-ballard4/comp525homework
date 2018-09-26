"""
Comp 525
h1.py
Ryan Ballard
9/26/2018
"""

def circle_area(radius):
    """
    Calculates the area of a circle with given radius.
    radius: non-negative float
    Returns: float
    """
    import math
    area = ( radius* radius * math.pi)
    return area

 #circle_area() To call fill in parameters



def is_even(number):
    """
    Checks if number is even
    number: integer
    Returns: True if number is even, False otherwise
    """
    if number % 2 == 0:
        return True
    else:
        return 

#is_even() To call fill in parameters 

def sum_of_1_to_n(n):
    """
    Calculates the sum of integers from 1 to given n
    n: positive integer
    Returns: integer
    """
    y = 0 
    for x in range (1 + n):
        y = y + x
    return y

#sum_of_1_to_n() To call fill in parameters

def miles_per_gallon(miles, gallons):
        """
         Calculates miles per gallons
         miles: positive float
         gallons: positive float
        """       
        mpg = miles / gallons
        return mpg
# miles_per_gallon(x,y) To call fill in two parameters

def sum_ten_random_1_10_interval( ):
    """
    Returns sum of  ten random integers in [1, 10]   interval
    """
    import random
    random_numbers =int
    sum = 0

    for x in range (10):
        random_numbers = random.randint(1,10)
        sum = random_numbers + sum
    return sum
# sum_ten random_1_10_interval () To call function

def average_odd_1_to_n(n):
    """
    Calculates the average of odd integers
    between 1 and given n
    n: positive integer 
    Returns: integer
    """
    from statistics import mean
    average = int
    average = mean (range(1, n + 1, 2))
    return average
# average_odd_1_to_n () To call fill in parameter




