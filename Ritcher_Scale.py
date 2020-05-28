# -*- coding: utf-8 -*-
"""
Write a program that reads a magnitude from the user and displays the appropriate
descriptor as part of a meaningful message. For example, if the user enters 5.5 then
your program should indicate that a magnitude 5.5 earthquake is considered to be a
moderate earthquake.
"""

earthquake_magnitude=(input("Enter an earthquake magnitude:"))
em=float(earthquake_magnitude)

if(em < 2.0):
    print("Magnitude %.1f earthquake is considered to be a micro earthquake." %em)
elif(em>=2.0 and em<3.0):
    print("Magnitude %.1f earthquake is considered to be a very minor earthquake." %em)
elif(em>=3.0 and em<4.0):
    print("Magnitude %.1f earthquake is considered to be a minor earthquake." %em)
elif(em>=4.0 and em<5.0):
    print("Magnitude %.1f earthquake is considered to be a light earthquake." %em)
elif(em>=5.0 and em<6.0):
    print("Magnitude %.1f earthquake is considered to be a moderate earthquake." %em)
elif(em>=6.0 and em<7.0):
    print("Magnitude %.1f earthquake is considered to be a strong earthquake." %em)
elif(em>=7.0 and em<8.0):
    print("Magnitude %.1f earthquake is considered to be a major earthquake." %em)
elif(em>=8.0 and em<10.0):
    print("Magnitude %.1f earthquake is considered to be a great earthquake." %em)
elif(em>=10.0):
    print("Magnitude %.1f earthquake is considered to be a meteoric earthquake." %em)

    