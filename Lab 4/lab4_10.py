"""
    Program: lab4_10.py
    Author: Michael Rouse
    Date: 9/12/13
    Description: Gets two numbers from the user and outputs different solutions
"""
print("Tell me two numbers and I will show you some math solutions for that number\n\n\n")

first = int(input("First number: "))
second = int(input("Second number: "))

print(first, "+", second, "=", first + second)
print(first, "-", second, "=", first - second)
print(first, "*", second, "=", first * second)
print(first, "/", second, "=", first / second)
print(first, "//", second, "=", first // second)

print("\n\nDone...")
