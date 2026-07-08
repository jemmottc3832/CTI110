# Christopher Jemmott
# p4lab2
# 7/8/26
# Write a program that asks the user to enter an integer

run_again = "yes"

while run_again == "yes":
    user_num = int(input("Enter an integer: "))
    print()

    if user_num >= 0:
        # For loop to print the multiplication table from 1 to 12
        for i in range(1, 13):
            print(f"{user_num}*{i} = {user_num * i}")
    else:
        # Handles negative integer input
        print("This program does not handle negative numbers.")

    print()
    run_again = input("Would you like to run the program again? "). lower()
    print()

    print("Exiting program...")
            
            
            