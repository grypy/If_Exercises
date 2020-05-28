# -*- coding: utf-8 -*-
"""
Write a program that reads a year from the user and displays the animal associated
with that year. Your program should work correctly for any year greater than or equal
to zero, not just the ones listed in the table.
"""
year=int(input("Enter the year (chinese zodiac):"))
print("\n\nAccording to the Chinese zodiac calendar." )
if(year%12 == 8):
    print("\nYear %d is Dragon" %year)
elif(year%12 == 9):
    print("\nYear %d is Snake" %year)
elif(year%12 == 10):
    print("\nYear %d is Horse" %year)
elif(year%12 == 11):
    print("\nYear %d is Sheep" %year)
elif(year%12 == 0):
    print("\nYear %d is Monkey" %year)
elif(year%12 == 1):
    print("\nYear %d is Rooster" %year)
elif(year%12 == 2):
    print("\nYear %d is Dog" %year)
elif(year%12 == 3):
    print("\nYear %d is Pig" %year)
elif(year%12 == 4):
    print("\nYear %d is Rat" %year)
elif(year%12 == 5):
    print("\nYear %d is Ox" %year)
elif(year%12 == 6):
    print("\nYear %d is Tiger" %year)
elif(year%12 == 7):
    print("\nYear %d is Hare" %year)
