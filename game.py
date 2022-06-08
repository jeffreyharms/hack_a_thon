from classes.ninja import Ninja
from classes.pirate import Pirate
import random

turn = random.randint(1,2)



michaelangelo = Ninja("Michaelangelo")
jack_sparrow = Pirate("Jack Sparrow")

def play_again():
    choice = input("Would you like to play again? y/n")
    if choice == "y":
        play = True
        michaelangelo.__init__("Michaelangelo")
        jack_sparrow.__init__("Jack Sparrow")
    else: 
        play = False 
    return play

print("Thanks for playing")

play = True

Ninja.compare_speed(michaelangelo.speed, jack_sparrow.speed)
while play == True:
    if turn == 1:
        michaelangelo.choose_action(jack_sparrow)
        if jack_sparrow.health <= 0:
            play = False
        turn = 2    
    if turn == 2:
        jack_sparrow.choose_action(michaelangelo)
        if michaelangelo.health <= 0:
            play = False
        turn = 1
