# christopher jemmott
# 7/7/2026
# p4hw1
# a program that collects scores,validates them, drops the lowest, and calculates the average and letter grade.

# ask the user to enter the number of scores they would like to enter
num_scores = int(input("How many scores would you like to enter? "))
print()

# initialize empty list
score_list = []

# create a loop to collect the number of scores
for i in range(1, num_scores + 1):
    score = float(input(f"Enter score #{i}: "))

    # Evaluate if the score is valid
    if score < 0 or score > 100:
        # If the score is invalid, loop until a valid score is entered
        while score < 0 or score > 100:
            print("\nINVALID Score entered!!!!")
            print("Score should be between 0 and 100.")
            score = float(input(f"Enter score #{i}: again: "))
            # Add the corrected valid score  to the list
    score_list.append(score)
else:
    # If the score was valid on the first try, add directly to the list
    score_list.append(score)

    # After collecting all scores, find the lowest score
    lowest = min(score_list)

    # Remove the lowest score
    score_list.remove(lowest)

    # Calculate average
    average = sum(score_list) / len(score_list)

    # Determine letter grade
    if average >= 90:
        letter_grade = 'A'
    elif average >= 80:
        letter_grade = 'B'
    elif average >= 70:
        letter_grade = 'C'
    elif average >= 60:
        letter_grade = 'D'
    else:
        letter_grade = 'F'

    # Display Results
    print("\n-------------------Results-------------------")
    print(f"Lowest Score  : {lowest}")
    print(f"Modified List : {score_list}")
    print(f"Scores Average: {average:.2f}")
    print(f"Grade         : {letter_grade}")
    print("---------------------------------------------")

