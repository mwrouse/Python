"""
    Program: power_function.py
    Author: Michael Rouse
    Date: 10/30/13
    Description: Create a function power(base, exponent)
"""

def power(base, exponent):
    """ Function to handle exponents """
    answer = 1

    # Find the answer
    for i in range(exponent):
        answer *= base

    # Return the answer
    return answer


print(power(2, 3))
print(power(6, 8))

    
    
