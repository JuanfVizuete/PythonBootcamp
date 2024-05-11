print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
print("You are at a crossroads. To the left is a dark forest, to the right is a beautiful river with a rainbow.")
choice1 = input("Which way do you want to go? Type 'left' or 'right'.\n").lower()
if choice1 == "left":
  print("You walk into the dark forest and are attacked by a werewolf. Game over.")
else:
  print("You walk along the river and come to a lake. There is an island in the middle of the lake.")
  choice2 = input("Do you want to swim to the island or wait for a boat? Type 'swim' or 'wait'.\n").lower()
  if choice2 == "swim":
    print("You swim to the island and are attacked by a crocodile. Game over.")
  else:
    print("You wait for a boat and arrive at the island safely. You see a house with three main doors of different colors.")
    choice3 = input("Which door do you want to open? Type 'red', 'yellow' or 'blue'.\n").lower()
    if choice3 == "red":
      print("You open the red door and are attacked and burned by a dragon. Game over.")
    elif choice3 == "yellow":
      print("You open the yellow door and find a treasure chest full of gold and jewels. You WIN!!")
    elif choice3 == "blue":
      print("You open the blue door and are attacked and eaten by a beast. Game over.")
    else:
      print("You chose a door that doesn't exist. Game over.")
