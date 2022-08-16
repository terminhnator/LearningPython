from tkinter import *

window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

def convert_miles_to_km():
    miles = float(input.get())
    km = round(miles * 1.609, 2)
    result.config(text=f"{km}")




# [Entry] Entry box

input = Entry(width=10)
input.get()
input.grid(column=1, row=0)

# [Label] Miles

miles_label = Label(text="Miles", font=("Courier"))
miles_label.grid(column=2, row=0)

# [Label] Is equal to

equal_label = Label(text="is equal to", font=("Courier"))
equal_label.grid(column=0, row=1)

#### [Label] Result in km

result = Label(text="0", font=("Courier"))
result.grid(column=1, row=1)

# [Label] Km
km_label = Label(text="Km", font=("Courier"))
km_label.grid(column=2,row=1)

# Calculate button

calc_button = Button(text="Calculate", command=convert_miles_to_km)
calc_button.grid(column=1,row=2)

window.mainloop()
