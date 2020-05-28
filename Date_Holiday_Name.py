# -*- coding: utf-8 -*-
"""
Write a program that reads a month and day from the user. If the month and day
match one of the holidays listed previously then your program should display the
holiday’s name. Otherwise your program should indicate that the entered month and
day do not correspond to a fixed-date holiday.
"""
month=input("Enter the name of the month:")
day=int(input("Enter the day of the month:"))

if((month == "january" or month == "January" or month == "JANUARY") and day == 1):
    print("\nNew year's day")
elif((month == "july" or month == "July" or month == "JULY") and day == 1):
    print("\nCanada day")
elif((month == "december" or month == "December" or month == "DECEMBER") and day == 25):
    print("\nChristmas day")
else:
    print("Does nto correspond to a fixed-date holiday")
