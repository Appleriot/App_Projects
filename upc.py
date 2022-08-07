import json
import requests
import pandas as pd
import os
import tkinter as tk

from tkinter import *
from openpyxl import load_workbook

window = tk.Tk()
window.geometry('600x500')
window.title("Upc SpreadSheet")
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

title_label = tk.Label(window, text="Upc SpreadSheet Marker", bg='#FFD700')
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

def create_text():
    try:
        inp = inputtxt.get(1.0, "end-1c")
        url = f"https://api.upcdatabase.org/product/{inp}?apikey=FB853379393C7E85F47C03B69EF7E412"
        repose = requests.get(url)
        print(os.path.exists("excel.xlsx"))
        if os.path.exists("excel.xlsx") == False:
            with open(inp, 'w') as f:
                json.dump(repose.json(), f, indent=2)
            information = repose.json()
            if 'metadata' in information:
                del information['metadata']
            title = information['title']
            df = pd.DataFrame(information, index=[title[0:10]]).to_excel("excel.xlsx")
            old_label_names.config(text="The file was created.", fg='black')

        else:
            workbook = load_workbook('excel.xlsx')
            worksheet = workbook.active
            information = repose.json()
            if 'metadata' in information:
                del information['metadata']
            worksheet.append([information['title'], information['description'], information['brand'], information['barcode']])
            workbook.save('excel.xlsx')
            old_label_names.config(text="The file was updated.", fg='black')

    except Exception as error:
        old_label_names.config(text="Did you misspell it?")
        print(error)

inputtxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
inputtxt.pack()

old_label_names = tk.Label(window, text='', wraplength=1200, justify="left", bg='#FFD700')
old_label_names.pack(padx=10, pady=10)

# Button Creation
printButton = tk.Button(window,
                        text = "Enter",
                        command = create_text,
                        bg='#4a7abc',
                        fg='black',
                        activebackground='green',
                        activeforeground='white',)
printButton.pack()

window.mainloop()
