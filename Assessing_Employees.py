# -*- coding: utf-8 -*-
"""
Write a program that reads a rating from the user and indicates whether the performance was unacceptable, acceptable or meritorious. The amount of the employee’s
raise should also be reported. Your program should display an appropriate error
message if an invalid rating is entered
"""

Raise = 2400
rating= float(input("Enter a rating on performance:"))
if(rating == 0.0):
    print("Unacceptable performance")
    amount=Raise*rating
    print("Employee's raise: $%.2f" %amount)
elif(rating == 0.4):
    print("Acceptable performance")
    amount=Raise*rating
    print("Employee's raise: $%.2f" %amount)
elif(rating == 0.6):
    print("Meritorious performance")
    amount=Raise*rating
    print("Employee's raise: $%.2f" %amount)
else:
    print("Not a valid rating.")
