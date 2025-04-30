# Dice Rolling Game

# The idea is to create a dice rolling game where the user can roll 2 dies and get a random number between 1 and 6.
# The user will be asked if they want to roll the dice again and the game will continue until the user decides to stop.
# • Modify the program so the user can specify how many dice they want to roll. 


# Importing the random function module
import random as r

def dice_rolling_game():
    
    count = 0 # To count the number of times the dice was thrown
    while True:    
        user_input = input("Do you want to throw the dice : (Y/N) ").lower()
        if user_input == 'y':
            user_input_int = int(input("How many dice do you want to throw : ")) 
            for i in range(user_input_int):
                rand3 = r.randint(1,6) # Generates a random number between 1 to 6
                print(rand3,end=" ")
            count += 1 # Increments the counter by 1 for every dice is thrown

            print()
        elif user_input == 'n':
            print(f'The user has rolled the dice {count} times.')
            print("Thank you for playing")
            break
        else:
            print("Invalid input entered") 
            print("Please enter either Y or N.")
            continue


dice_rolling_game()

