"""
    Program: repeat_it_code.py
    Author: Michael Rouse
    Date: 10/24/13
    Description: Daily Design Exercise, create a function called repeat it that repeats a message
                  multiple times.
"""

def repeat_it(message = "\n", multiplier = 1):
    """ Repeats message the amount of times as the multiplier """

    # Add a line break to the message
    message += "\n"

    # Print the message the amount of times as the multiplier
    print(message * multiplier)



