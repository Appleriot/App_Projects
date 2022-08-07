import tkinter as tk
import pymongo

from trycourier import Courier
from os.path import exists
from tkinter import *

password = "teentitan"
client = Courier(auth_token='pk_prod_Q6QC5FAXNXM1ZPKZQDJ49JTKK97V')

window = tk.Tk()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()
window.geometry(f'{screen_width}x{screen_height}')
window.title("4 u 2 u")
window.config(padx=10, pady=10, bg='#74F2CE')

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

title_label = tk.Label(window, text="4 u 2 u", bg='#74F2CE')
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

def create_collection():
    person_name = persontxt.get(1.0, "end-1c")
    name = inputtxt.get(1.0, "end-1c")
    num_name = deltetxt.get(1.0, "end-1c")
    product_name = productstxt.get(1.0, "end-1c")
    date_name = datetxt.get(1.0, "end-1c")
    message = f'{person_name}, {name}, {num_name}, {product_name}, {date_name}'
    try:
        myclient = pymongo.MongoClient("mongodb://Doakes:pokemonmaster@cluster0-shard-00-00.svxda.mongodb.net:27017,cluster0-shard-00-01.svxda.mongodb.net:27017,cluster0-shard-00-02.svxda.mongodb.net:27017/?ssl=true&replicaSet=atlas-93gp11-shard-0&authSource=admin&retryWrites=true&w=majority")
        mydb = myclient.test
        mycollection = mydb["customors"]
        if exists("collections names.txt"):
            with open('collections names.txt', 'w') as f:
                f.write(f'{person_name}')
        else:
            f = open("collections names.txt", "w+")
            f.write(f"{person_name}")
        dicts = {'name': person_name, 'address': name, 'phone number': num_name, "products":product_name, "date": date_name}
        x = mycollection.insert_one(dicts)
        myclient.close()
        resp = client.send(
            event="courier-quickstart",
            recipient="ditaeviondoakes@gmail.com",
            data={
                "infromation": f'{message}'
            },
            profile={
                "email": "ditaeviondoakes@gmail.com"
            }
        )
        old_label_names.config(text="Your information was sent.")
    except Exception as error:
        old_label_names.config(text=f"{error}")
        print(error)

persontxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
persontxt.pack()

inputtxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
inputtxt.pack()

deltetxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
deltetxt.pack()

productstxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
productstxt.pack()

datetxt = tk.Text(window,
                   height = 2,
                   width = 20,
                   fg='red')
datetxt.pack()

old_label_names = tk.Label(window, text='', wraplength=1200, justify="left", bg='#74F2CE')
old_label_names.pack(padx=10, pady=10)

# Button Creation
printButton = tk.Button(window,
                        text = "Sumbit",
                        command = create_collection,
                        bg='#561D25',
                        fg='#F25F5C',
                        activebackground='green',
                        activeforeground='white',)
printButton.pack()

checks_names = tk.Label(window, text='First Box:Name, Second Box:Address, Thrid Box:Phone Number, Fourth Box:Products Names, Fifth Box: Date of Delivery', wraplength=1200, justify="left", bg='#74F2CE')
checks_names.pack(padx=20, pady=20)

window.mainloop()

