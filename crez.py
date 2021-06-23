import csv
import tkinter as tk
import random
import time

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = tk.Tk()
window.geometry('600x500')
window.title("Creative respone")
window.config(padx=10, pady=10)

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

title_label = tk.Label(window, text="Information on Slaves During 1600's-1950's")
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

filename = 'toc.csv'
with open(filename) as f:
    reader = csv.reader(f)
    header_row = next(reader)

    full = {'all':[]}
    new = []
    for row in reader:
        author = str(row[1])
        title = str(row[2])
        url = str(row[4])

        neck = author,title,url

        full['all'].append(neck)

for ans in full['all']:
    new.append(ans)

old_label_names = tk.Label(window, text=f'{random.choice(new)}', wraplength=1200, justify="left")
old_label_names.config(font=('Arial', 11))
old_label_names.pack(pady=10, padx=10)

class New:
    def reset():
        old_label_names.destroy()
        label_names = tk.Label(window, text=f'{random.choice(new)}', wraplength=1200, justify="center").place(x=0, y=100)
    def clean():
        label_names.after(1, label_names.master.destroy)

reset = Button(text="Reset", command=New.clean and New.reset)
reset.pack()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo, cursor="target")
    label.image = photo #avoid garbage collection

image = Image.open('civil_war_soldiers.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

window.mainloop()
