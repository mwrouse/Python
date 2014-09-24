"""
    Program:
    Author: Michael Rouse
    Date: 11/22/13
    Description: Calculate number of cans donated
"""

cans = 300
ramen = 1000
cash = 124.33

total = int(300 + (1000 / 3) + (124.33 * 3))


print("Cans: "+str(cans))
print("Ramen: "+str(ramen))
print("Cash: $"+str(cash))
print("\nTotal cans (Rounded): "+str(total))
