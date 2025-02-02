# Rock, Paper and Scissors game

'''
The game will prompt the player to choose rock, paper, or scissors by typing 'r',
'p', or 's'. The computer will randomly select its choice. The game will then display
both choices using emojis and determine the winner based on the rules.

'''
import random as r

def rock_paper_scissors():
    choices = ['r','p','s']
   # computer = r.choice(choices)
    attempts = 5
    computer_score = 0
    user_score = 0
    tie = 0
    while True:
        i = 0
        while i < attempts:
            user_input = input("Rock,Paper,Scissors (r/p/s): ").lower()
            print((f'User : {user_input}'))
            computer = r.choice(choices)
            print(f'Computer : {computer}')
            if computer == 'p':
                if user_input == 'r':
                    computer_score += 1
                elif user_input == 's':
                    user_score += 1
                elif user_input == 'p':
                    tie += 1
            elif computer == 's':
                if user_input == 'p':
                    computer_score += 1
                elif user_input == 'r':
                    user_score += 1
                elif user_input == 's':
                    tie += 1
            elif computer == 'r':
                if user_input == 'p':
                    user_score += 1
                elif user_input == 's':
                    computer_score += 1
                elif user_input == 'r':
                    tie += 1
            i += 1
        print(f'Computer Score : {computer_score}')
        print(f'User Score : {user_score}')
        print(f'Ties : {tie}')
        if computer_score > user_score:
            print("Computer Won")
            break
        elif computer_score == user_score:
            print("Tie Game")
        else:
            print("User Won")
            break

rock_paper_scissors()