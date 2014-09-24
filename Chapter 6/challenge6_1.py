"""
    Program: challenge6_1.py
    Author: Michael Rouse
    Date: 10/14/13
    Description: Improves the ask_number() function so the function can be called with a step value.
                 Make default step value equal to 1
"""
def ask_number(question, low, high, step=1):
    """Ask for a number within a range."""
    response = None
    while response not in range(low, high, step):
        response = int(input(question))

    return response

# Test the function by asking for an even number between 0 and 100
print(ask_number("Enter an even number between 0 and 100: ", 0, 100, 2))
