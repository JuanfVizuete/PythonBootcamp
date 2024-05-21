#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

from art import logo
import random

print(logo)
print("Welcome to the Number Guessing Game! by Juan Vizuete")
print("I'm thinking of a number between 1 and 100.")
# Generate a random number between 1 and 100
number = random.randint(1, 100)
print(f"Pssst, the correct answer is {number}")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
else:
  attempts = 5

def guess_number(attempts):
  """Function to play the game to guess the number"""
  #global attempts
  while attempts > 0:
    print(f"You have {attempts} attempts remaining to guess the number.")
    guess = int(input("Make a guess: "))
    if guess == number:
      print(f"You got it! The answer was {number}.")
      attempts = -1
    elif guess > number:
      print("Too high.")
    else:
      print("Too low.")
      
    attempts -= 1

    if attempts == 0:
      print("You've run out of guesses, you lose.")
    elif attempts > 0:
      print("Guess again.")
  
guess_number(attempts)
