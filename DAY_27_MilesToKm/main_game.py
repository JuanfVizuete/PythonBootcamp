# Mile to Kilometers Converter Project by Juan Vizuete
from tkinter import *

FONT = ("Arial", 14)

window = Tk()
window.title('Mile to Km Converter')
window.minsize(width=400, height=200)
window.config(padx=40, pady=40)

label_miles = Label(text="Miles", font=FONT)
label_miles.grid(column=2, row=0)
label_equal = Label(text="is equal to", font=FONT)
label_equal.grid(column=0, row=1)
label_km = Label(text="Km", font=FONT)
label_km.grid(column=2, row=1)

miles_entry = Entry(width=10, font=FONT)
miles_entry.grid(column=1, row=0)

def calculate_km():
     miles = miles_entry.get()
     resultado = float(miles) * 1.609
     label_result.config(text=f"{resultado:.3f}")

button_calculate = Button(text="Calculate", font=FONT, command=calculate_km)
button_calculate.grid(column=1, row=2)

label_result = Label(text="0", font=FONT)
label_result.grid(column=1, row=1)

window.mainloop()
