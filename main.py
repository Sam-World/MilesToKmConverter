from tkinter import *


# calculate function
def calculate():
    result = float(number.get()) * 1.609
    label_3["text"] = result


# window
window = Tk()
window.title("Miles to Km Converter")
window.config(padx=20, pady=20)

# entry
number = Entry(width=7)
number.grid(column=1, row=0)

# label: Miles
label_1 = Label(text="Miles", font=("Arial", 12))
label_1.grid(column=2, row=0)

# label: is equal to
label_2 = Label(text="is equal to", font=("Arial", 12))
label_2.grid(column=0, row=1)

# label: print results
label_3 = Label(text="0", font=("Arial", 12))
label_3.grid(column=1, row=1)

# label: km
label_4 = Label(text="Km", font=("Arial", 12))
label_4.grid(column=2, row=1)

# button: calculate
button = Button(text="calculate", command=calculate)
button.grid(column=1, row=2)

window.mainloop()
