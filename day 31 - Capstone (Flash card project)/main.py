from tkinter import *
from random import *

import pandas
import pandas as pd

BACKGROUND_COLOR = "#B1DDC6"
to_learn = {}
current_card = {}

# ---------------------- CREATE FLASH CARDS ----------------------------- #

try:
    data = pd.read_csv("./data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pandas.read_csv("./data/german_words.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")


def next_card():
    global current_card, flip_timer
    window.after_cancel(flip_timer)
    current_card = choice(to_learn)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_card["German"], fill="black")
    canvas.itemconfig(canvas_image, image=card_back_img)
    flip_timer = window.after(3000, func=flip_card)


def right_answer():
    to_learn.remove(current_card)
    new_data = pandas.DataFrame(to_learn)
    new_data.to_csv("./data/words_to_learn.csv", index=False)
    next_card()


# ---------------------------FLIP CARD------------------------------------#

def flip_card():
    canvas.itemconfig(canvas_image, image=card_front_img)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_card["English"], fill="white")


# --------------------------- UI SETUP ---------------------------------- #

# Window

window = Tk()
window.title("Language Flash Cards")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

flip_timer = window.after(3000, func=flip_card)

# Canvas

canvas = Canvas(width=800, height=526, bg=BACKGROUND_COLOR, highlightthickness=0)
card_back_img = PhotoImage(file="./images/card_front.png")
card_front_img = PhotoImage(file="./images/card_back.png")
canvas_image = canvas.create_image(400, 263, image=card_back_img)
card_title = canvas.create_text(400, 150, fill="black", font=("Arial", 40, "italic"), text="Title")
card_word = canvas.create_text(400, 263, fill="black", font=("Arial", 60, "bold"), text="Word")

canvas.grid(row=0, column=0, columnspan=2)

# Wrong Button

wrong_button_img = PhotoImage(file="./images/wrong.png")
wrong_button = Button(image=wrong_button_img, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

# Right Button

right_button_img = PhotoImage(file="./images/right.png")
right_button = Button(image=right_button_img, highlightthickness=0, command=right_answer)
right_button.grid(row=1, column=1)


next_card()

window.mainloop()
