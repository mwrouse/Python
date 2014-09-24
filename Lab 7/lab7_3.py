"""
    Program: lab7_3.py
    Author: Michael Rouse
    Date: 9/27/13
    Description: Picks a random car from the tuple, trims the tuple. In the end it will display the fine for
                 the car picked
"""

print("""
                Let me pick a random car for you and tell you the fine!
    """)
import random

cars = ("Ferrari", "Corvette", "DeLorean", "Mercedes", "Chevrolet")

# Total fines
totalFine = 0

# Array of cars picked in their order
carsPicked = ()

# For-Loop will execute 5 times
for i in range(0, 5):
    if i == 0:
        input("\nPress Enter to pick a car...")
    else:
        input("\nPress Enter to pick another car...")
        
    carNum = random.randrange(0, len(cars))
    print("\nYou picked a", cars[carNum])

    # Add the picked car to the carsPicked tuple
    carsPicked += cars[carNum: carNum + 1]
    
    # Trim the cars tuple
    cars = cars[:carNum] + cars[carNum + 1: len(cars)]
        
# Tell the user the cars they picked and their fines   
print("\n\nHere are all the cars you picked and their speeding ticket fines:\n")

for i in range(len(carsPicked)):
    car = carsPicked[i]
    
    if car == "Ferrari":
        fine = 200
    elif car == "Corvette":
        fine = 100 
    elif car == "DeLorean":
        fine = 175
    elif car == "Mercedes":
        fine = 50
    else:
        fine = 0

    totalFine += fine
    
    print(car, "= $", fine)

print("\nTotal fine: $", totalFine)



input("\nPress the Enter key to exit...")
     
