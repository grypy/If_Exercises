# -*- coding: utf-8 -*-
"""
The length of a month varies from 28 to 31 days. In this exercise you will create
a program that reads the name of a month from the user as a string. Then your
program should display the number of days in that month. Display “28 or 29 days”
for February so that leap years are addressed.
"""
month=input("Enter the name of the month(in block letters):")
if(month=="JANUARY" or month == "MARCH" or month == "MAY" or month == "JULY" or month == "AUGUST" or month == "OCTOBER" or month == "DECEMBER"):
    print("%s has 31 days" %month)
elif(month == "FEBRUARY"):
    print("%s has 28 or 29 days" %month)
elif(month == "APRIL" or month == "JUNE" or month == "SEPTEMBER" or month == "NOVEMBER"):
    print("%s has 30 days" %month)
else:
    print("Invalid entry!!!")
    
        
