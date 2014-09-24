"""
    Program: dd24.py
    Author: Michael Rouse
    Date: 11/19/13
    Description: Daily Design 24. Program that prints three more zeros each time the user types in
                 Enter.
"""
times_to_print = 3

user_input = ""

while user_input.lower() != "q":
    print("0" * times_to_print)

    times_to_print += 3

    user_input = input("More? ")


input("\n\nPress the Enter key to exit...")
