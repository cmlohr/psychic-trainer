import random
from replit import clear 
from art import logo
from art import logo2
#Starting header
print(logo)
print(logo2)
start_game = input("                                      Press 'ENTER/RETURN' to play.").lower()
if start_game == "":
    clear()

def game():
    cont = True
    while cont:
        guess = int(random.choice(range(1,101)))
        #print(guess) #prints guess for testing
        level = 0

#difficulty level setup
        difficulty = input("Set your difficulty- type 'easy' or 'hard':\n> ").lower()
        if difficulty == "easy":
            level = 10
            print("You have 10 attempts")
        elif difficulty == "hard":
            level = 5
            print("You have 5 attempts")
        else:
            print("Invalid Input")

#FIRST GUESS
        player_guess = int(input("Guess a number:\n> "))
        if player_guess == guess:
            print("Correct!  You Win")
        if player_guess < guess:
            print("Too low.")
        if player_guess > guess:
            print("Too High.")

#IF THE GUESS DOES NOT EQUAL THE NUMBER LOOP
        while player_guess != guess:
            level = level - 1 #LEVEL CALCULATION
            score = level
            print(f"Attempts left: {score}")
            player_guess = int(input("Guess again:\n> "))
            if player_guess < guess:
                print("Too low.")
            if player_guess > guess:
                print("Too High.")
            if level <= 1:
                print("No more attempts, you lose!")
                break

        

#RESTART OR EXIT
        if input("Play again? Type 'y' or 'n':\n> ").lower() == "y":
            clear()
            game()  
        else:
            clear()
            cont = False
            
                 
game()