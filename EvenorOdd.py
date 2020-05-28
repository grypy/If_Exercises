# -*- coding: utf-8 -*-
"""
Write a program that reads an integer from the user. Then your program should
display a message indicating whether the integer is even or odd
"""
val=int(input("Enter an integer:"))
if(val%2 == 0):
    print("%d is an even number" %val)
elif(val%3 == 0):
    print("%d is an odd number" %val)
else:
    print("%d is a prime number" %val)
    