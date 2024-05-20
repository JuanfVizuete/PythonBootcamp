############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

#MY GAME BLACKJACK - JUAN VIZUETE

import random
from replit import clear
from art import logo

#FUNCTIONS
def deal_card():
  """Returns a random card from the deck."""
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  card = random.choice(cards)
  return card

def calculate_score(cards):
  """Take a list of cards and return the score calculated from the cards"""
  if 11 in cards and sum(cards) > 21:
    cards.remove(11)
    cards.append(1)
  if sum(cards) == 21:
    return 21
  return sum(cards)
  
def compare(user_score, computer_score):
  """Compares the user and computer scores and returns the result"""
  if user_score == computer_score:
    return "Draw 🙃"
  elif user_score > 21 and computer_score > 21:
    return "You both lose 😤"
  elif computer_score == 21:
    return "Lose, opponent has Blackjack 😱"
  elif user_score == 21:
    return "Win with a Blackjack 😎"
  elif user_score > 21:
    return "You went over. You lose 😭"
  elif computer_score > 21:
    return "Opponent went over. You win 😁"
  elif user_score > computer_score:
    return "You win 😃"
  else:
    return "You lose 😤"

def play_game_blackjack():
  """Plays a game of Blackjack"""
  if input("Do you want to play a game of Blackjack? Type 'y' or 'n': ") == "y":
    clear()
    print(logo)
    #USER CARDS
    user_cards = []
    #COMPUTER CARDS
    computer_cards = []
    #DEALING CARDS
    for i in range(2):
      user_cards.append(deal_card())
      computer_cards.append(deal_card())
    user_score = calculate_score(user_cards)
    computer_score = calculate_score(computer_cards)
   
    print(f"Your cards: {user_cards}, current score: {user_score}")
    print(f"Computer's first card: {computer_cards[0]}")
  
    end_game = False
    another_card = "y"
    while not end_game:
    
      if user_score == 21 or computer_score == 21 or another_card == "n" or user_score > 21:
        print(f"Your final hand: {user_cards}, final score: {user_score}")
        print(f"Computer's final hand: {computer_cards}, final score: {computer_score}")
        print(compare(user_score, computer_score))
        end_game = True
        play_game_blackjack()
      else:
        if calculate_score(computer_cards) < 17:
          computer_cards.append(deal_card())
          computer_score = calculate_score(computer_cards)
        another_card = input("Type 'y' to get another card, type 'n' to pass: ")
        if another_card == "y":
          user_cards.append(deal_card())
          user_score = calculate_score(user_cards)
          print(f"Your cards: {user_cards}, current score: {user_score}")
          print(f"Computer's first card: {computer_cards[0]}")
    
  else:
    print("Goodbye")

play_game_blackjack()
