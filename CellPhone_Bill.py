# -*- coding: utf-8 -*-
"""
Write a program that reads the number of minutes and text messages used in a
month from the user. Display the base charge, additional minutes charge (if any),
additional text message charge (if any), the 911 fee, tax and total bill amount. Only
display the additional minute and text message charges if the user incurred costs in
these categories. Ensure that all of the charges are displayed using 2 decimal places.

A particular cell phone plan includes 50 minutes of air time and 50 text messages
for $15.00 a month. Each additional minute of air time costs $0.25, while additional
text messages cost $0.15 each. All cell phone bills include an additional charge of
$0.44 to support 911 call centers, and the entire bill (including the 911 charge) is
subject to 5 percent sales tax.
"""

print("CELL PHONE BILL")
minutes=float(input("Enter number of minutes used:"))
texts=float(input("Enter the number of text messages sent:"))

Sale_tax = 0.05
CC_991 = 0.44
add_min = 0.25
add_txt = 0.15

if(minutes <= 50 or texts <=50):
    Base_charge = 15.00
    amount = Base_charge + CC_991
    amount_after_tax = amount+ (amount*Sale_tax)
    
    print("\n\n CELL PHONE BILL RECEIPT")
    print("Base charge: $%.2f" %Base_charge)
    print("911 fee: $%.2f" %CC_991)
    print("Sale tax: $%.2f" %Sale_tax)
    print("Total bill amount: $%.2f" %amount_after_tax)
    print("No additional minutes charge")
    print("No additional text message charge")

elif(minutes > 50 and texts > 50):
    Base_charge = 15.00    
    min_add_cost = (minutes-50)*add_min
    txt_add_cost = (texts-50)*add_txt
    amount = Base_charge + CC_991 + min_add_cost + txt_add_cost
    amount_after_tax = amount+ (amount*Sale_tax)
    
    print("\n\nCELL PHONE BILL RECEIPT")
    print("Base charge: $%.2f" %Base_charge)
    print("911 fee: $%.2f" %CC_991)
    print("Sale tax: $%.2f" %Sale_tax)
    print("Additional minutes charge: $%.2f" %min_add_cost)
    print("Additional text message charge: $%.2f" %txt_add_cost) 
    print("Total bill amount: $%.2f" %amount_after_tax)
    