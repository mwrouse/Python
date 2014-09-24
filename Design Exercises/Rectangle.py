"""
    Program: Rectangle.py
    Author: Michael Rouse
    Date: 12/16/13
    Description: Create a class definition called Rectangle
"""

class Rectangle(object):
    """ Class for Rectangle Object """
    def __init__(self, length=1, width=1):
        self.__length = length
        self.__width = width

    def get_length(self):
        """ Get rectangle length """
        return self.__length
        
    def set_length(self, new_length=1):
        """ Set the length """
        if self.__checkInput(new_length):
            self.__length = int(new_length)
        
    def get_width(self):
        """ Get the width """
        return self.__width

    def set_width(self, new_width=1):
        """ Set the width """
        if self.__checkInput(new_width):
            self.__width = int(new_width)
            
    def __checkInput(self, var):
        """ Make sure input is valid """
        try:
            int(var)

        except:
            return False

        else:
            return True
        
    @property
    def perimeter(self):
        """ Get the perimeter of the rectanlge """
        perimeter = (2 * self.__length) + (2 * self.__width)

        return perimeter
    
    @property
    def area(self):
        """ Get the area of the rectangle """
        area = self.__length * self.__width

        return area
