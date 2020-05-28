# -*- coding: utf-8 -*-
"""
Write a program that reads a sound level in decibels from the user. If the user
enters a decibel level that matches one of the noises in the table then your program
should display a message containing only that noise. If the user enters a number
of decibels between the noises listed then your program should display a message
indicating which noises the level is between. Ensure that your program also generates
reasonable output for a value smaller than the quietest noise in the table, and for a
value larger than the loudest noise in the table
"""
noise=int(input("Enter the noise level(dB):"))
if(noise == 130):
    print("Noise level: Jackhammer")
elif(noise == 106):
    print("Noise level: Gas Lawnmower")
elif(noise == 70):
    print("Noise level: Alarm clock")
elif(noise == 40):
    print("Noise level: Quiet room")
elif(noise>40 and noise<70):
    print("Noise level between Quiet room and Alarm clock")
elif(noise>70 and noise<106):
    print("Noise level between Alarm clock and Gas lawnmower")
elif(noise>106 and noise<130):
    print("Noise level between Gas lawnmower and Jackhammer")
elif(noise<40):
    print("Noise level lower than Quiet room")
elif(noise>130):
    print("Noise level greater than Jackhammer")
else:
    print("Invalid entry")