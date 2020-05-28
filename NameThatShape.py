# -*- coding: utf-8 -*-
"""
Write a program that determines the name of a shape from its number of sides. Read
the number of sides from the user and then report the appropriate name as part of
a meaningful message. Your program should support shapes with anywhere from 3
up to (and including) 10 sides. If a number of sides outside of this range is entered
then your program should display an appropriate error message
"""

side=int(input("Enter the number of sides:"))
if(side<3):
    print("Invalid entry!!!")
elif(side == 3):
    print("Triangle")
elif(side == 4):
    print("Rectangle or square")
elif(side == 5):
    print("Pentagon")
elif(side == 6):
    print("Hexagon")
elif(side == 7):
    print("Heptagon")
elif(side == 8):
    print("Octagon")
elif(side == 9):
    print("Nonagon")
elif(side == 10):
    print("Decagon")
        
        
