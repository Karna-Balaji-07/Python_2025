# Number guessing Game
'''
Write a program to have the computer randomly select a number between 1 and
100, and then prompt the player to guess the number.
The program should give hints if the guess is too high or too low.

 1. Allow the user to specify the minimum and maximum values for the number
range before the game starts. This gives the player more control over the
difficulty level. 



'''
import random as r

def number_guessing():
    minimum = int(input("Enter the Minimum value : "))
    maximum = int(input("Enter the maximum value : "))
    random_number = r.randint(minimum,maximum)
    limit = 5
    attempt = 0
    while True:
        try:
            user_input = int(input("Guess a number: "))
            print("Your guessed Number is : ",user_input)
            i = 0
            attempt += 1
            while i < limit: 
                if user_input > random_number:
                    print("Too high")
                elif user_input < random_number:
                    print("Too low")
                else:
                    print("You have guessed the correct number")
                    break
            else:
                print("You havee exceeded the maximum limit for guessing the number.")
                print(f' The Number is {random_number}')
        except ValueError:
            print("Please enter a number in the range 1 to 100")

number_guessing()