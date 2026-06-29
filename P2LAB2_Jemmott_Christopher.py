#christopher jemmott
#6/27/2026
#P2LAB2
#write a program that creates a dictionary where the key and value pairs are as follows

cars = {"Camero":18.21,"prius":52.36,"models":110,"silverado":26 }

#get keys from dictionary
cars_keys = cars.keys() 

print(cars_keys)

print(*cars_keys, sep=", ")

#get a car from user
car_name = input("Enter a car: ")

#get mpg for the given car
car_mpg = cars[car_name]

print(f"The {car_name} gets {car_mpg} miles per gallon")

#get miles from user
miles_driven = float(input(f"How many miles will you drive the {car_name}? "))

#calculate
gallons_needed = miles_driven / car_mpg

#display results
print(f"{gallons_needed} gallon(s) of gas are needed to drive the {car_name} {miles_driven} miles")