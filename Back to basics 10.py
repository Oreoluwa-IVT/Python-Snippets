#You are welcome the the "GUESS THE NUMBER PROGRAM"
import random

random_number=random.randint(1,100)
player_number=int(input("Guess the Number"))

guesses=1

while player_number != random_number:
    if player_number> random_number:
        player_number=int(input("Try a Smaller Number"))
        guesses+=1
    elif player_number<random_number:
        player_number=int(input("Try a Bigger Number"))
        guesses+=1
    elif player_number==random_number:
        print("Weldone! You guess the number right")
        print("It took you a number of guesses though. ",guesses," to the precise")
    else:
        print("Huh , what was that. Please try again jare")
        player_number=int(input("Try again"))
        
    

