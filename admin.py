import tkinter as tk
import pymongo

from os.path import exists
from tkinter import *

window = tk.Tk()
window.geometry('600x500')
window.title("4 u 2 u")
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

title_label = tk.Label(window, text="Database handler", bg='#FFD700')
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

def find_lastest():
    try:
        myclient = pymongo.MongoClient("mongodb://Doakes:pokemonmaster@cluster0-shard-00-00.svxda.mongodb.net:27017,cluster0-shard-00-01.svxda.mongodb.net:27017,cluster0-shard-00-02.svxda.mongodb.net:27017/?ssl=true&replicaSet=atlas-93gp11-shard-0&authSource=admin&retryWrites=true&w=majority")
        mydb = myclient.test
        mycollection = mydb["customors"]
        for z in mycollection.find({},{ "_id": 0, "name": -1, "address": -1, "phone number": -1, "products": -1, "date":-1 }):
            old_label_names.config(text=f"{z}")

    except Exception as error:
        print(error)
        old_label_names.config(text="A error has happened.")

def deltee():
    delete = deltetxt.get(1.0, "end-1c")
    try:
        myclient = pymongo.MongoClient("mongodb://localhost:27017/")
        mydb = myclient["mydatabase"]
        f = open("collections names.txt", "r")
        mycollection = mydb[f"{f.read()}"]
        myquery = {"address": f"{delete}"}
        mycollection.delete_one(myquery)
    except Exception as error:
        old_label_names.config(text="A error has happened.")

deltetxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
deltetxt.pack()

old_label_names = tk.Label(window, text='', wraplength=1200, justify="left", bg='#FFD700')
old_label_names.pack(padx=10, pady=10)

findbutton = tk.Button(window,
    text="Find",
    command=find_lastest,
    bg='#4a7abc',
    fg='black',
    activebackground='green',
    activeforeground='white',)
findbutton.pack()

deltebutton = tk.Button(window,
    text="Delete",
    command=deltee,
    bg='#4a7abc',
    fg='black',
    activebackground='green',
    activeforeground='white',)
deltebutton.pack()

checks_names = tk.Label(window, text='Type in name of person and hit Delete to remove person.', wraplength=1200, justify="left", bg='#FFD700')
checks_names.pack(padx=10, pady=10)

window.mainloop()
