"""
    Program: gross_pay.py
    Author: Michael Rouse
    Date: 10/28/13
    Description: Daily Design Exercise. Create a function to calculate gross pay, as well as overtime pay
"""

def gross_pay(hourlyRate, hoursWorked):
    """ Calculate the gross pay of an employee """
    
    # Determine if the employee has overtime
    if hoursWorked <= 40:
        # No overtime

        pay = hourlyRate * hoursWorked

    else:
        # Has overtime

        pay = hourlyRate * 40
        
        # Get amount of overtime hours
        hoursWorked -= 40

        # Calculate overtime pay
        hourlyRate = hourlyRate + (hourlyRate / 2)

        # Calculate overtime
        pay += hourlyRate * hoursWorked

    # Return pay to main program
    return pay


        
    
