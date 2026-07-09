# Christopher Jemmott
# LLM_Jemmott_Christopher
# 7/8/26

import random

def play_guessing_game():
    session_history = []
    round_number = 1

    print("Welcome to the Number Guessing Game!") 
    print("Type 'quit' at any time to exit.\n")
    while True:
        secret_number = random.randint(1, 100)
        attempts_taken = 0
        game_status = "quit"  # Default to quit, changes to 'won' if they guess it correctly

        print(f"--- Round {round_number} ---")
        print("I am thinking of a number between 1 and 100.")

        # Inner loop for the active round
        while True:
            user_input = input("Enter your guess: ").strip().lower()

            if user_input == 'quit':
                break

            # Input Validation to ensure the user types a number
            if not user_input.isdigit():
                print("Invalid input. Please enter a number or 'quit'.")
                continue

            guess = int(user_input)
            attempts_taken += 1

            if guess < secret_number:
                print("Too Low!")
            elif guess > secret_number:
                print("Too High!")
            else:
                print(f"Correct! You guessed the number in {attempts_taken} attempts.")      
                game_status = "won"
                break

        # Create the dictionary for this round
        round_data = {
            "round_number": round_number,
            "secret_number": secret_number,
            "attempts_taken": attempts_taken,
            "game_status": game_status
        }

        # Append the dictionary to our tracking list
        session_history.append(round_data)

        # If the user quit during the round, break the main loop entirely
        if game_status == "quit":
            break

        # Ask to play again if they won the round
        play_again = input("\nWould you like to play again? (yes/no): ").strip().lower()
        if play_again != 'yes':
            break

        round_number += 1
        print() 

    # Display the final session history
    print("\n=== Session History ===")
    for record in session_history:
        print(record)

# Run the game
if __name__ == "__main__":
    play_guessing_game()


