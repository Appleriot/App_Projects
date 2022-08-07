import csv
import random
import tkinter as tk
import time

from tkinter import *
from tkinter import ttk
from PIL import Image, ImageTk

window = Tk()
window.geometry('600x600')
window.title("Jobs recommecation")
window.config(padx=10, pady=10, bg='white')

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

title_label = Label(window, text="Jobs post and salarys")
title_label.config(font=("Lobster", 34, ),fg='red', cursor="target")
title_label.pack(padx=10, pady=10)

filename = 'Best_Jobs.csv'
with open(filename, encoding="utf8") as f:
    reader = csv.reader(f)
    base = {'all':[]}

    for row in reader:
        salary = row[0]
        edcuation = row[1]
        title = row[4]
        skills = row[5]
        country = row[6]
        location_site = row[8]
        neck  = salary, edcuation, title, skills, country, location_site

        base['all'].append(neck)

good_ansewer = []
bad_answers = []

for ans in base['all']:
    good_ansewer.append(ans)
    if "Unknown" or "," or "</div>" in ans:
        bad_answers.append(neck)
    else:
        pass

o = Label(window, text=f'Jobs info: {random.choice(good_ansewer)}.', cursor="target", fg="red", wraplength=1200, justify="left")
o.config(font=('Arial', 12))
o.pack(padx=10, pady=10)

def reset():
    o.destroy()
    label_names = Label(window, text=f'Jobs info: {random.choice(good_ansewer)}.',
        wraplength=1200, justify="center", fg="red").place(x=0, y=100)
    label_names.destroy()

def resize_image(event):
    new_width = event.width
    new_height = event.height
    image = copy_of_image.resize((new_width, new_height))
    photo = ImageTk.PhotoImage(image)
    label.config(image = photo, cursor="target")
    label.image = photo #avoid garbage collection

reset = Button(text="Reset", command=reset)
reset.pack()

image = Image.open('bread.png')
copy_of_image = image.copy()
photo = ImageTk.PhotoImage(image)
label = ttk.Label(window, image = photo)
label.bind('<Configure>', resize_image)
label.pack(fill=BOTH, expand = YES)

window.mainloop()
