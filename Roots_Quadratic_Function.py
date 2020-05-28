# -*- coding: utf-8 -*-
import math
"""
Write a program that computes the real roots of a quadratic function. Your program
should begin by prompting the user for the values of a, b and c. Then it should display
a message indicating the number of real roots, along with the values of the real roots
(if any).
"""
print("Univariate quadratic function f(x)=ax^2+bx+c")
a=float(input("Enter the coefficient a:"))
b=float(input("Enter the coefficient b:"))
c=float(input("Enter the coefficient c:"))

print("\n\n")
d = (math.pow(b,2))-(4*a*c)  #discriminant
if(d == 0):
    print("The equation has one real root")
    root=-b/(2*a)
    print("root: %.2f" %root)
    
elif(d < 0):
    print("The equation does not have any real roots")
    r1=(-b+1j*math.sqrt(d/-1))/(2*a)
    r2=(-b-1j*math.sqrt(d/-1))/(2*a)
    print("Root 1:", r1)
    print("Root 2:", r2)
elif(d > 0):
    print("The equation has two real roots")
    r1=(-b+math.sqrt(d))/(2*a)
    r2=(-b-math.sqrt(d))/(2*a)
    print("Root 1:", r1)
    print("Root 2:", r2)
