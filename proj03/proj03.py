# Name: Reid Chandler
# Date: 6/20/17


""" 
proj 03: Guessing Game
s
Generate a random number between 1 and 9 (including 1 and 9). 
Ask the user to guess the number, then tell them whether they guessed too low, too high, 
or exactly right. Keep the game going until the user types exit.
Keep track of how many guesses the user has taken, and when the game ends, print this out.

"""
import random

y= "yes"
while y== "yes" or "yeah" or "ye" or "yep":
    guess=0
    variable_name=random.randint(1,9)
    x=int(raw_input("Guess a number between 1 and 9: "))
    while x != variable_name:
        if guess!=2:
            if x>variable_name:
                print "Too big."
                x = int(raw_input("Guess again: "))
                guess=guess+1
            elif x<variable_name:
                print "Too small."
                x = int(raw_input("Guess again: "))
                guess=guess+1
        else:
            print "Sorry, you lost. The correct answer was" , variable_name
            y = raw_input("Want to try again?: ")
            y=y.lower()
            guess = 0
            break

    if x== variable_name:
        print "Congratulations," , variable_name , "is correct"
        print "You took" , guess+1 , "turns"
        y= raw_input("Do you want to keep going?(yes or no): ")
    if y == "no" or "nah" or "nope":
        print "The End"