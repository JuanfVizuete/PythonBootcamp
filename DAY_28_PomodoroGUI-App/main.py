from tkinter import *
import math
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    window.after_cancel(timer)
    # time 00:00
    canvas.itemconfig(timer_text, text="00:00")
    # title label reset
    title_label.config(text="Timer", fg=GREEN)
    # reset check marks
    check_label.config(text="")
    # reset de repetitions too
    global reps
    reps = 0

# ---------------------------- TIMER MECHANISM ------------------------------- # 

def start_timer():
    global reps
    reps += 1
    work_sec = WORK_MIN * 60
    short_break_sec = SHORT_BREAK_MIN * 60
    long_break_sec = LONG_BREAK_MIN * 60

    # If its the 8th rep
    if reps % 8 == 0:
        title_label.config(text="Break", fg=RED)
        count_down(long_break_sec)
    elif reps % 2 == 0:
        # if its 2nd/4th/6th rep:
        title_label.config(text="Break", fg=PINK)
        count_down(short_break_sec)
    else:
        # If its the 1st/3rd/5th/7th rep
        title_label.config(text="Work", fg=GREEN)
        count_down(work_sec)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 

# Window loop al final del programa ya es un loop que revisa que cambia a cada momento
# takes an amount of time that should wait and then call a particular function
def count_down(count):
    # Obtener los minutos y segundos en formato tiempo
    count_min = math.floor(count / 60)
    count_sec = count % 60
    # Dynamic typing (variables change types easily)
    if count_sec < 10:
        count_sec = f"0{count_sec}"

    # To change the text in the canvas, we have to call the canvas first and then itemconfig
    canvas.itemconfig(timer_text, text=f"{count_min}:{count_sec}")
    if count > 0:
        global timer
        timer = window.after(1000, count_down, count - 1)
    else:
        start_timer()
        check_symbol = ""
        working_sessions = math.floor(reps / 2)
        for i in range(working_sessions):
            check_symbol += "✔"
        check_label.config(text=check_symbol)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

canvas = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)   # correct the background color
tomato_img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=tomato_img)    # Los valores de X y Y se les pone para ponerlos en la mitad de la ventana
timer_text = canvas.create_text(100, 130, text="00:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)


title_label = Label(text="Timer", font=(FONT_NAME, 35, "bold"), fg=GREEN, bg=YELLOW)
title_label.grid(column=1, row=0)

start_button = Button(text="Start", font=FONT_NAME, highlightthickness=0, command=start_timer)
start_button.grid(column=0, row=2)
reset_button = Button(text="Reset", font=FONT_NAME, highlightthickness=0, command=reset_timer)
reset_button.grid(column=2, row=2)

check_label = Label(font=(FONT_NAME, 18, "bold"), fg=GREEN, bg=YELLOW)
check_label.grid(column=1, row=3)


window.mainloop()

