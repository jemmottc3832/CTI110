# christopher jemmott
# 6-25-2026
# p1hw2
# program that calculates and displays travel expenses based on a user's budget.

print("This program calculates and displays travel expenses")
print()

budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")

print()

gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

print()

total_expenses = gas + accommodation + food
remaining_balance = budget - total_expenses