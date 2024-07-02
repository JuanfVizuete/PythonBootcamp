from tkinter import *
import pandas
import random


BACKGROUND_COLOR = "#B1DDC6"
current_card = {}

try:
    data = pandas.DataFrame(pandas.read_csv("data/words_to_learn.csv"))
except FileNotFoundError:
    data = pandas.DataFrame(pandas.read_csv("data/polish_words.csv"))

data_list = data.to_dict(orient="records")


def pick_random_card():
    global current_card, flip_timer
    # with the flip timer variable you control de button action to wait for the flip card
    window.after_cancel(flip_timer)
    current_card = random.choice(data_list)
    canvas.itemconfig(card_background, image=card_front)
    canvas.itemconfig(language_text, text="Polish", fill="black")
    canvas.itemconfig(word_text, text=current_card["Polish"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_background, image=card_back)
    canvas.itemconfig(language_text, text="English", fill="white")
    canvas.itemconfig(word_text, text=current_card["English"], fill="white")

def is_known():
    data_list.remove(current_card)
    new_data = pandas.DataFrame(data_list)
    new_data.to_csv("data/words_to_learn.csv", index=False)   #words still to learn, index False doesnt include de index so it doesnt repeat
    pick_random_card()

window = Tk()
window.title("Flashy Card Game")
window.config(background=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, func=flip_card)

# Creating canvas
canvas = Canvas(width=800, height=526, background=BACKGROUND_COLOR, highlightthickness=0)
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
card_background = canvas.create_image(400, 263, image=card_front)
language_text = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
word_text = canvas.create_text(400, 263, text="", font=("Arial", 60, "bold"))
canvas.grid(row=0, column=0, columnspan=2)

# Creating buttons
wrong_img = PhotoImage(file="images/wrong.png")
right_img = PhotoImage(file="images/right.png")
wrong_button = Button(image=wrong_img, highlightthickness=0, padx=50, pady=50, command=pick_random_card)
wrong_button.grid(row=1, column=0)
right_button = Button(image=right_img, highlightthickness=0, padx=50, pady=50, command=is_known)
right_button.grid(row=1, column=1)

pick_random_card()

window.mainloop()