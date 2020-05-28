# -*- coding: utf-8 -*-
"""
Create a program that reads a month and day from the user. The user will enter
the name of the month as a string, followed by the day within the month as an
integer. Then your program should display the season associated with the date that
was entered.
"""

month=input("Enter the name of the month:")
day=int(input("Enter the day of the month:"))

if((month == "March" or month == "march" or month == "MARCH") or day == 20):
    print("\nFirst day of spring")
    
elif((month == "June" or month == "june" or month == "JUNE") or day == 21):
    print("\nFirst day of summer")

elif((month == "September" or month == "september" or month == "SEPTEMBER") or day == 22):
    print("\nFirst day of fall")
    
elif((month == "December" or month == "december" or month == "DECEMBER") or day == 21):
    print("\nFirst day of winter")
else:
    print("\n\nNot a first day of any season")

