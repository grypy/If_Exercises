# -*- coding: utf-8 -*-
"""
Write a program that implements the conversion from human years to dog years
described in the previous paragraph. Ensure that your program works correctly for
conversions of less than two human years and for conversions of two or more human
years. Your program should display an appropriate error message if the user enters
a negative number.
"""
n=float(input("Enter human years:"))
if (n<0):
    print("Negative number!!!")
if(n>=0 and n<=2):
    dog_years=10.5*n
    print("Dog Years: %.2f yrs" %dog_years)
elif(n>2):
    dog_years=(2*10.5)+((n-2)*4)
    print("Dog Years: %.2f yrs" %dog_years)
else:
    print("Invalid entry")
    
        
        