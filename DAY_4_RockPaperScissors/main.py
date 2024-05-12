rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
import random

print("Welcome to the Rock, Paper, Scissors game! by Juan Vizuete")
options = [rock, paper, scissors]
choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors.\n"))
computer_option = random.randint(0,2)
if choice >= 0 or choice <= 2:
    print(options[choice])
else:
    print("You typed an invalid number, you lose!")

print("Computer chose:")
print(options[computer_option])
if (choice == 0 and computer_option == 2) or (choice == 1 and computer_option == 0) or (choice == 2 and computer_option == 1):
    print("You win!")
elif choice == computer_option:
    print("It's a draw")
else:
    print("You lose :(")
