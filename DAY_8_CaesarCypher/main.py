alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

#PART 4
#TODO-3: What happens if the user enters a number/symbol/space?
#Can you fix the code to keep the number/symbol/space when the text is encoded/decoded?
#e.g. start_text = "meet me at 3"
#end_text = "•••• •• •• 3"

def caesar(text, shift, direction):
    cipher_text = ""
    letter_index = 0
    for letter in text:
        if letter in alphabet:  #checks if the letter is in the alphabet, otherwise is a number or symbol or space
            letter_index = alphabet.index(letter)
            if direction == "encode" and letter_index + shift >= len(alphabet):
                cipher_text += alphabet[letter_index + shift - len(alphabet)]
            elif direction == "decode" and letter_index - shift < 0:
                cipher_text += alphabet[letter_index - shift + len(alphabet)]
            elif direction == "encode":
                cipher_text += alphabet[letter_index + shift]
            elif direction == "decode":
                cipher_text += alphabet[letter_index - shift]
        else:
            cipher_text += letter

    print(f"The {direction}d text is {cipher_text}")

#PART 4
#TODO-1: Import and print the logo from art.py when the program starts.
from art import logo
print(logo)
#TODO-4: Can you figure out a way to ask the user if they want to restart the cipher program?
#e.g. Type 'yes' if you want to go again. Otherwise type 'no'.
#If they type 'yes' then ask them for the direction/text/shift again and call the caesar() function again?
#Hint: Try creating a while loop that continues to execute the program if the user types 'yes'. 
restart = "yes"
while (restart == "yes"):
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    shift = shift % len(alphabet)
    caesar(text, shift, direction)
    restart = input("Type 'yes' if you want to go again. Otherwise type 'no'. \n")

#PART 4
#TODO-2: What if the user enters a shift that is greater than the number of letters in the alphabet?
#Try running the program and entering a shift number of 45.
#Add some code so that the program continues to work even if the user enters a shift number greater than 26. 
#Hint: Think about how you can use the modulus (%).
