# christopher jemmott
# 7/7/2026
# p4hw2
# a program that calculates gross pay for multiple employees and total amounts paid for overtime, regular hours, and gross pay.

# Initialize running totals
num_employees = 0
total_overtime_pay = 0.0
total_regular_pay = 0.0
total_gross_pay = 0.0

# Initial prompt for employee name
emp_name = input('Enter employee\'s name or "Done" to terminate: ')

# Loop until the user enters "Done"
while emp_name.lower() != "done":

    # Get hours and pay rate
    hours_worked = float(input(f"How many hours did {emp_name} work? "))
    pay_rate = float(input(f"What is {emp_name}'s pay rate? "))
    print()

    # Calculate pay components
    if hours_worked > 40:
        regular_hours = 40
        overtime_hours = hours_worked - 40
    else:
        regular_hours = hours_worked
        overtime_hours = 0

    # Calculate amounts
    regular_pay = regular_hours * pay_rate
    overtime_pay = overtime_hours * (pay_rate * 1.5)
    gross_pay = regular_pay + overtime_pay 

    # Add to running totals
    num_employees += 1
    total_overtime_pay += overtime_pay
    total_regular_pay += regular_pay
    total_gross_pay += gross_pay

    # Display individual employee results
    print(f"Employee names: {emp_name}")
    print()
    print(f"{'Hours Worked':<15}{'Pay Rate':<12}{'Overtime':<12}{'Overtime Pay':<15}{'Regular Pay':<15}{'Gross Pay':<15}")
    print("-" * 80)
    print(f"{hours_worked:<15.1f}{pay_rate:<12.2f}{overtime_hours:<12.1f}{overtime_pay:<15.2f}${regular_pay:<14.2f}${gross_pay:<14.2f}")
    print("\n")

    # Prompt for the next employee to continue or break the loop
    emp_name = input('Enter employee\'s name or "Done" to terminate: ')

# display final grade totals once the loop ends
print()
print(f"Total number of employees entered: {num_employees}")
print(f"Total amount paid for overtime: ${total_overtime_pay:.2f}")
print(f"Total amount paid for regular pay: ${total_regular_pay:.2f}")
print(f"Total amount paid for gross pay: ${total_gross_pay:.2f}")
