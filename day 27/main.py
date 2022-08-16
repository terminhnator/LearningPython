from tkinter import *

window = Tk()
window.title("My First GUI program")
window.minsize(width=500,height=300)
window.config(padx=20, pady=20)

#Label

my_label = Label(text="I am a label", font=("Courier", 24, "bold"))
my_label.config(text="New Text")
my_label.grid(column=0, row=0)

#Button

def button_clicked():
    print("I got clicked")
    new_text = input.get()
    my_label.config(text=new_text)

button = Button(text="Click Me", command = button_clicked)
button.grid(column=1,row=1)

#Entry

input = Entry(width=10)
input.get()
print(input.get())
input.grid(column=3,row=2)

#New BUtton
new_button = Button(text="New Button")
new_button.grid(column=2,row=0)

window.mainloop()
