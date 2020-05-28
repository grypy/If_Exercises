# -*- coding: utf-8 -*-
import math
"""
Write a program that reads the frequency of the radiation from the user and displays
the appropriate name.
"""
freq=float(input("Enter the frequency for the electromagnetic radiation:"))
if(freq < (3*math.pow(10,9))):
    print("Radio waves")
elif(freq >= (3*math.pow(10,9)) and (freq < math.pow(10,12))):
    print("Microwaves")
elif(freq >= (3*math.pow(10,12)) and (freq < (4.3*math.pow(10,14)))):
    print("Infrared Light")
elif(freq >= (4.3*math.pow(10,14)) and (freq < (7.5*math.pow(10,14)))):
    print("Visible light")
elif(freq >= (7.5*math.pow(10,14)) and (freq < (3*math.pow(10,17)))):
    print("Ultraviolet light")
elif(freq >= (3*math.pow(10,17)) and (freq < (3*math.pow(10,19)))):
    print("X-rays")
elif(freq > (3*math.pow(10,19))):
    print("Gamma rays")

