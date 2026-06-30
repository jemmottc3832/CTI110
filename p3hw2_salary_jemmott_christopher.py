# christopher jemmott
# 06-29-2026
# p3hw2_salary
# this program calculates an employee's regular hours pay, overtime pay, and total gross pay based on user inputs.

# Prompt the user to enter the employee's name.
# Prompt the user to enter the number of hours worked.
# Prompt the user to enter the employee's hourly pay rate.
# Check IF hours worked is greater than 40:
# - overtime hours = hours worked - 40
# - overtime pay = overtime hours * (pay rate * 1.5)
# - regular hours pay = 40 * pay rate
# ELSE:
# - overtime hours = 0
# - overtime pay = 0.0
# - regular hours pay = hours worked * pay rate
# calculate gross pay = regular hours pay + overtime pay
# display the employee's name and structured payroll table matching the required template.

# request user inputs
employee_name = input("Enter the employee's name: ")
hours_worked = float(input("Enter the number of hours worked: "))
pay_rate = float(input("Enter the employee's hourly pay rate: "))

# determine overtime and calculate pay breakdown 
if hours_worked > 40:
    overtime_hours = hours_worked - 40
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    regular_pay = 40 * pay_rate
else:
    overtime_hours = 0.0
    overtime_pay = 0.0
    regular_pay = hours_worked * pay_rate

# calculate gross pay
gross_pay = regular_pay + overtime_pay

# display the formatted output matching the assignment example
print("-" * 35)
print(f"Employee Name: {employee_name}\n")

# Format and print table headers
print(f"{'Hours Worked':<15}{'Pay Rate':,<12}{'OverTime':<12}{'OverTime Pay':<17}{'RegHour Pay':<15}{'Gross Pay'})")
print("-" * 80)

# print values aligned with headers, formatting currency to 2 decimal places where appropriate
print(f"{hours_worked:<15.1f}{pay_rate:<12.1f}{overtime_hours:<12.1f}${overtime_pay:<16.2f}${regular_pay:<14.2f}${gross_pay:.2f}")
