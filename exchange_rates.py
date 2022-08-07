import csv
import tkinter as tk
import random
import time

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('600x500')
window.title("Exchange Finder")
window.config(padx=10, pady=10, bg='#FFD700')

f = Frame(window)

xscrollbar = Scrollbar(f, orient=HORIZONTAL)
xscrollbar.grid(row=1, column=0, sticky=N+S+E+W)

yscrollbar = Scrollbar(f)
yscrollbar.grid(row=0, column=1, sticky=N+S+E+W)

text = Text(f, wrap=NONE,
            xscrollcommand=xscrollbar.set,
            yscrollcommand=yscrollbar.set)
text.grid(row=0, column=0)

xscrollbar.config(command=text.xview)
yscrollbar.config(command=text.yview)

title_label = tk.Label(window, text="Exchange of Different Countries", bg='#FFD700')
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

filename = 'exchange_rates.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    full = {'all':1,}

    for row in reader:
        names = str(row[2]).lower()
        values = str(row[3])

        full[f'{names}'] = f'{values}'

def create_text():
    try:
        inp = inputtxt.get(1.0, "end-1c")
        old_label_names.config(text="Currency: "+ full[inp.lower()], fg='black')
    except Exception:
        old_label_names.config(text="Did you misspell it?")

class New:
    def reset():
        if failed_label_names == True:
            failed_label_names.destroy()
        else:
            old_label_names.destroy()
        old_label_names.config(text="Currency:"+ full[inp])
    def clean():
        old_label_names.after(1, label_names.master.destroy)

inputtxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
inputtxt.pack()

old_label_names = tk.Label(window, text='', wraplength=1200, justify="left", bg='#FFD700')
old_label_names.pack(padx=10, pady=10)

# Button Creation
printButton = tk.Button(window,
                        text = "Currency",
                        command = create_text,
                        bg='#4a7abc',
                        fg='black',
                        activebackground='green',
                        activeforeground='white',)
printButton.pack()

reset = Button(text="Reset", command=New.clean and New.reset,bg='#4a7abc',
                    fg='yellow', activebackground='red', activeforeground='white',)
reset.pack()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo, cursor="target")
    label.image = photo #avoid garbage collection

image = Image.open('money.jpg')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

window.mainloop()
