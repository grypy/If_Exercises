# -*- coding: utf-8 -*-

"""
In this exercise you will create a program that reads a letter of the alphabet from the
user. If the user enters a, e, i, o or u then your program should display a message
indicating that the entered letter is a vowel. If the user enters y then your program
should display a message indicating that sometimes y is a vowel, and sometimes y is
a consonant. Otherwise your program should display a message indicating that the
letter is a consonant
"""

letter=input("Enter a letter from the alphabet:")
val=letter
if(val=='a' or val=='e' or val=='i' or val=='o' or val=='u'):
    print("Letter is a vowel")
elif(val=='A' or val=='E' or val=='I' or val=='O' or val=='U'):
    print("Letter is a vowel")
elif(val=='y' or val=='Y'):
    print("Y is vowel or consonant")
else:
    print("Letter is a consonant")
        
    