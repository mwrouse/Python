"""
    Program: challenge2_4.py
    Author: Michael Rouse
    Date: 8/29/13
    Description: Has user enter base car price and adds a bunch of fees
"""

carValue = int(input("What is the base car value you're looking for? "))
carTax = carValue * .25
carLicense = carValue * .35
dealerPrep = 2500
destChange = 1670

total = carValue + carTax + carLicense + dealerPrep + destChange

print("\nCar value: ", carValue)
print("Car Tax: ", carTax)
print("License Fee: ", carLicense)
print("Dealer Prep Fee: ", dealerPrep)
print("Destination Change Fee: ", destChange)
print("\nTotal: ", total)

print("\n\n\nDone...")
