# Christopher Jemmott
# July 19, 2026
# Final Project for Web Programming Class
# Air Fryer Simulator: Cook your meal perfectly without burning it!

import random
import time

def cook_meal(meal):
    print(f"\nPutting the {meal['protein']} in the air fryer...")

    #1. Using the time library
    time.sleep(1)

    #2. using the random library
    cook_time = random.randint(3, 7)
    print( "Air fryer is running...")

    for i in range(cook_time):
        print(f"Minute {i + 1}...")
        time.sleep(1)

        #3. Changing dictionary key:value pairs during gameplay
        meal["crispiness"] += 15

        if meal["crispiness"] > 50:
            meal["status"] = "burnt"
        elif meal["crispiness"] >= 45:
            meal["status"] = "perfect"
        elif meal["crispiness"] >= 30:
            meal["status"] = "cooked" 

    return meal

#4. Using functions (including main)
def main():
    print("welcome to the Air Fryer Simulator!")
    print("Lets's get dinner ready.\n")

    #5. Main object represented by a Python dictionary
    my_meal = {
        "protein": "Chicken Bites",
        "status": "raw",
        "crispiness": 0
    }

    print(f"Initial meal state: {my_meal}\n")

    action = input("Press 'C' and hit Enter to start cooking: ").upper()
    if action == "C":
        my_meal = cook_meal(my_meal)
        
        print("\nDing! Air fryer is done.")
        print(f"Final meal state: {my_meal}\n")

        #6. Non-violent/non-offensive gameplay logic
        if my_meal["status"] == "perfect":
            print("Golden and crispy! You win!")
        elif my_meal["status"] == "cooked":
            print("Its's cooked, but could be crispier. Good job!")
        elif my_meal["status"] == "burnt":
            print("Oh no! its burnt to a crisp! Game over.")
        else:
            print("It's still raw. Game over.")
    else:
        print("You decided not to cook. Game Over.")


if __name__ == "__main__":
    main() 
    
   
            
