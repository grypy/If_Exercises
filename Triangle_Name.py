# -*- coding: utf-8 -*-
"""
A triangle can be classified based on the lengths of its sides as equilateral, isosceles
or scalene. All 3 sides of an equilateral triangle have the same length. An isosceles
triangle has two sides that are the same length, and a third side that is a different
length. If all of the sides have different lengths then the triangle is scalene.
Write a program that reads the lengths of 3 sides of a triangle from the user.
Display a message indicating the type of the triangle
"""
s1=float(input("Enter the length of side 1:"))
s2=float(input("Enter the length of side 2:"))
s3=float(input("Enter the length of side 3:"))

if (s1 == s2 and s2 == s3 and s1 == s3):
    print("\nThis is an equilateral triangle.")

elif (s1 == s2 or s2 == s3 or s1 ==s3):
    print("\nThis is an isosceles triangle")

else:
    print("\n This is a scalene triangle")
