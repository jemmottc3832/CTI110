# christopher jemmott
# 06-29-2026
# P2HW2
# This program collects grades for 6 modules from the user, stores them in a list, and then calculates and displays the lowest grade, highest grade, sum of all grades, and average formatted to two decimal places.

# Ask the user to enter a grade for Module 1 and convert it to a float.
# Ask the user to enter a grade for Module 2 and convert it to a float.
# Ask the user to enter a grade for Module 3 and convert it to a float.
# Ask the user to enter a grade for Module 4 and convert it to a float.
# Ask the user to enter a grade for Module 5 and convert it to a float.
# Ask the user to enter a grade for Module 6 and convert it to a float.
# Create a list named 'grades' and store all six entered grades inside it.
# Find the lowest grade using the built-in min() function
# Find the highest grade using the built-in max() function
# calculate the sum of the grades using the built-in sum() function
# calculate the avergae by dividing the sum of the grades by the length of the list.
# display the results formatted exactly as shown in the example, aligning the values and rounding the average to two decimal places.

# Ask the user for the grades individually
grade1 = float(input("Enter grade for Module 1: "))
grade2 = float(input("Enter grade for Module 2: "))
grade3 = float(input("Enter grade for Module 3: "))
grade4 = float(input("Enter grade for Module 4: "))
grade5 = float(input("Enter grade for Module 5: "))
grade6 = float(input("Enter grade for Module 6: "))

# Store the grades in a list
grades = [grade1, grade2, grade3, grade4, grade5, grade6]

# calculate necessary metrics
lowest = min(grades)
highest = max(grades)
total = sum(grades)
average = total / len(grades)

# display the formatted results with exact alignment spacing
print("\n------------Results------------")
print(f"Lowest grade: {lowest}")
print(f"Highest grade: {highest}")
print(f"Sum of grades: {total}")
print(f"Average grade: {average:.2f}")
print("---------------------------------------")

