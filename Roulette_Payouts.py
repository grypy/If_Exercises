# -*- coding: utf-8 -*-
import random
"""
A roulette wheel has 38 spaces on it. Of these spaces, 18 are black, 18 are red, and two
are green. The green spaces are numbered 0 and 00. The red spaces are numbered 1,
3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30 32, 34 and 36. The remaining integers
between 1 and 36 are used to number the black spaces.
Many different bets can be placed in roulette. We will only consider the following
subset of them in this exercise:
• Single number (1 to 36, 0, or 00)
• Red versus Black
• Odd versus Even (Note that 0 and 00 do not pay out for even)
• 1 to 18 versus 19 to 36
Write a program that simulates a spin of a roulette wheel by using Python’s random
number generator. Display the number that was selected and all of the bets that must
be payed. For example, if 13 is selected then your program should display:
"""

print("Spin the wheel:")
print("\nROULETTE PAYOUTS")

val=random.randint(0,36)
print("The spin resulted in %d ..." %val)
if(val == 1 or val == 3 or val == 5 or val == 7 or val == 9 or val == 12 or val == 14 or val == 16 or val == 18 or val == 19 or val == 21 or val == 23 or val == 25 or val == 27 or val == 30 or val == 32 or val == 34 or val == 36):
    print("Pay %d" %val)
    print("Pay Red")
    
    if(val%2 == 0):
        print("Pay Even")
    else:
        print("Pay Odd")
        
    if(val>=1 and val<=18):
        print("Pay 1 to 18")
    elif(val>18 and val<=36):
        print("Pay 19 to 36")
    

elif(val == 2 or val == 4 or val == 6 or val == 8 or val == 10 or val == 11 or val == 13 or val == 15 or val == 17 or val == 20 or val == 22 or val == 24 or val == 26 or val == 28 or val == 29 or val == 31 or val == 33 or val == 35):
    print("Pay %d" %val)
    print("Pay Black")
    
    if(val%2 == 0):
        print("Pay Even")
    else:
        print("Pay Odd")
        
    if(val>=1 and val<=18):
        print("Pay 1 to 18")
    elif(val>18 and val<=36):
        print("Pay 19 to 36")

else:
    print("Pay 0 or Pay 00")
