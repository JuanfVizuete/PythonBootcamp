#Import libraries
import random
from art import logo, vs
from game_data import data
from replit import clear

#Crear lista y añadir la variable de data
instagram_accounts = data

#Functions
def random_account():
  """Returns a random account from the list"""
  return random.choice(instagram_accounts)

def format_data(account):
  """Format the account data into printable format"""
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess, a_followers, b_followers):
  """Checks followers against user's guess
  and returns True if they got it right."""
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

#Generate a random account from the game data
account_a = random_account()
account_b = random_account()
score = 0
print(logo)
def higher_lower_game(account_a, account_b, score):
  """Higher Lower Game"""  
  while (account_a == account_b):
    account_b = random_account()
  #game_continue = True
  print(f"Compare A: {format_data(account_a)}.")
  print(vs)
  print(f"Against B: {format_data(account_b)}.")
  guess = input("Who has more followers? Type 'A' or 'B': ").lower()

  clear()
  print(logo)
  if(check_answer(guess, account_a["follower_count"],     account_b["follower_count"])):
    score += 1
    print(f"You're right! Current score: {score}.")
    account_a = account_b
    account_b = random_account()
    higher_lower_game(account_a, account_b, score)
  else:
    print(f"Sorry, that's wrong. Final score: {score}")
    
  
higher_lower_game(account_a, account_b, score)


