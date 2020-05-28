# -*- coding: utf-8 -*-
"""
Write a program that begins by reading the denomination of a banknote from the
user. Then your program should display the name of the individual that appears on the
banknote of the entered amount. An appropriate error message should be displayed
if no such note exists.
"""
den=int(input("Enter the denomination of the banknote($): "))
if(den == 1):
    print("Individual: George Washington")
elif(den == 2):
    print("Individual: Thomas Jefferson")
elif(den == 5):
    print("Individual: Abraham Lincoln")
elif(den == 10):
    print("Individual: Alexander Hamilton")
elif(den == 20):
    print("Individual: Andrew Jackson")
elif(den == 50):
    print("Individual: Ulysses S. Grant")
elif(den == 100):
    print("Individual: Benjamin Franklin")
else:
    print("Bank notes not printed.")
