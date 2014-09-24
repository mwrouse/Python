"""
    Program: birthday.py
    Author: Michael Rouse
    Date: 10/29/13
    Description: Daily Design Exercise. Create a function that ask the user for the month, day, and year
                 of their birthday, turns it into a string and then returns the string.
"""

def get_birthday():
    """ Ask the user for information about their birthday and creates a string """
    # List of months and their numerical values
    months = {"january": "01", "february": "02", "march": "03", "april": "04", "may": "05", "june": "06",
              "july": "07", "august": "08", "september": "09", "october": "10", "november": "11",
              "december": "12"}

    # List of the amount of days in each month
    days = (0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31)

    # Inititalize variables
    month = ""
    day = 0
    year = 0

    # Ask user for month until they input a valid month
    while month.lower() not in months:
        month = input("What month were you born in (January, February, etc...)? ")

    # Convert the month to an integer
    month = int(months[month.lower()])

    # Ask user for the day until they input a valid one for that month
    while day <= 0 or day > days[month]:
        day = int(input("What day were you born on? "))

    # Ask user for the year
    year = int(input("What year were you born in? "))

    # Convert to a string
    birthday = str(month) + "-" + str(day) + "-" + str(year)

    # Return the birthday string
    return birthday

print(get_birthday())
    

    
