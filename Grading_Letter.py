# -*- coding: utf-8 -*-
"""
Write a program that begins by reading a letter grade from the user. Then your
program should compute and display the equivalent number of grade points. Ensure
that your program generates an appropriate error message if the user enters an invalid
letter grade.
"""
grade=input("Enter a letter grade:")

if(grade == "A+"):
    print("A+ --- 4.0 points")
elif(grade == "A"):
    print("A --- 4.0 points")
elif(grade == "A-"):
    print("A- --- 3.7 points")
elif(grade == "B+"):
    print("B+ --- 3.3 points")
elif(grade == "B"):
    print("B --- 3.0 points")
elif(grade == "B-"):
    print("B- --- 2.7 points")
elif(grade == "C+"):
    print("C+ --- 2.3 points")
elif(grade == "C"):
    print("C --- 2.0 points")
elif(grade == "C-"):
    print("C- --- 1.7 points")
elif(grade == "D+"):
    print("D+ --- 1.3 points")
elif(grade == "D"):
    print("D --- 1.0 points")
elif(grade == "F"):
    print("F --- 0 points")
else:
    print("Invalid entry !!!")
