import math


def polysum(n,s):
    """
    :param n: number of sides of polygon (int)
    :param s: length of those sides
    :return: area of polygon + perimeter of polygon squared. Rounded to 4dp.
    """
    # calculate and return area (left of '+') and add the square of the perimeter (right of '+')
    return round(0.25*n*s**2 / math.tan(math.pi/n) + (n*s)**2,4)
