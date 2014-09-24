"""
    Program: my_math.py
    Author: Michael Rouse
    Date: 10/17/13
    Description: Turn math problems into functions
"""

def cirlceArea(radius):
    """ Area of a Circle """
    area = 3.14 * (radius * radius)

    return area

def circleDiameter(radius):
    """ Diameter of a Circle """
    diameter = radius + radius

    return diameter

def circlePerimeter(radius):
    """ Perimeter of a Circle """
    perimeter = 3.14 * (radius + radius)

    return perimeter

def cylinderArea(radius, height):
    """ Area of a Cylinder """
    area = (2 * 3.14 * (radius * radius)) + (2 * 3.14 * radius * height)

    return area

def cylinderVolume(radius, height):
    """ Volume of a Cylinder """
    volume = 3.14 * (radius * radius) * height

    return volume

def prismArea(length, height, width):
    """ Area of a Prism """
    area = 2 * ((width * height) + (length * width) + (length * height))

    return area

def prismVolume(length, height, width):
    """ Volume of a Prism """
    volume = (width * length) * height

    return volume

def rectangleArea(length, width):
    """ Area of a Rectangle """
    area = length * width

    return area

def rectanglePerimeter(length, width):
    """ Perimeter of a Rectangle """
    perimeter = (2 * length) + (2 * width)

    return perimeter

def triangleArea(base, height):
    """ Area of a Triangle """
    area = (base * height) / 2

    return area
