#christopher jemmott
#6/27/2026
#P2LAB1
#This program performs mathematical calculations and displays information to users.



#import math module to use the constant, math.pi
import math

#get radius from user
radius = float(input("What is the radius of the circle? "))
print()

#calculate diameter
diameter = 2 * radius

#display diameter with 1 decimal point
print(f"the diameter of the circle is {diameter:.1f}\n")

#calculate circumference
circumference = 2 * math.pi * radius

#display circumference with 2 decimal places
print(f"the circumference of the circle is {circumference:.2f}\n")

#calculate the area
area = math.pi * radius ** 2

#display area with 3 decimal places
print(f"the area of the circle is {area:.3f}\n")



