"""
    Program: dd30.py
    Author: Michael Rouse
    Date: 12/10/13
    Description: Create a class called location and add attributes and methods
"""

class Location(object):
    """ Location Class """
    def __init__(self, longitude, latitude):
        self.__longitude = longitude
        self.__latitude = latitude
        self.__nearObjects = []     # Objects around the location

    def get_location(self):
        """ Print the location """
        print("Your location: " + self.__longitude + " " + self.__latitude)
        print("Objects you're near: " + self__.nearObjects)
        
    
    def change_location(self, city, state, zip_code):
        """ Modify location """
        self.__longitude = longitude
        self.__latitude = latitude
        self.__nearObjects = []
