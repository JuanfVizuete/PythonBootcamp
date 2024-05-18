from replit import clear
from art import logo
#HINT: You can call clear() to clear the output in the console.

print(logo)
bids = {}
more_bidders = "yes"
print("Welome to the secret auction program! by Juan Vizuete")

def add_bid(name, bid):
  bids[name] = bid

def highest_bidder():
  highest_bid = 0
  winner = ""
  for bidder in bids:
    bid_amount = bids[bidder]
    if bid_amount > highest_bid:
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner} with a bid of ${highest_bid}")
  
while(more_bidders == "yes"):
  name = input("What is your name?: ")
  bid = int(input("What is your bid?: $"))
  add_bid(name, bid)
  more_bidders = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if more_bidders == "yes":
    clear()

clear()
highest_bidder()
