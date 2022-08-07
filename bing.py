import tkinter as tk

from tkinter import *
from bing_image_downloader.downloader import download

window = tk.Tk()
window.geometry('600x500')
window.title("Dataset maker")
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

title_label = tk.Label(window, text="Dataset Creator")
title_label.config(font=("Lobster", 34))
title_label.pack(padx=10, pady=10)

def title_infomration():
    inp = inptext.get()
    name_output_dir = output_box.get()
    query_string = inp
    output_dir = name_output_dir
    try:
        download(query_string, limit=100, output_dir=output_dir, adult_filter_off=True, force_replace=False, timeout=100,
                    verbose=True)
        lbl = tk.label(window, text='The images are downloading.')
        lbl.pack()
    except Exception as error:
        lbl = tk.label(window, text=f'{error} has occured.')
        lbl.pack()

names = Label(window, text='Name of serach term: ')
names.pack()
inptext = Entry(window, fg='red')
inptext.pack()

outputt = Label(window, text='Name of output directory: ')
outputt.pack()
output_box = Entry(window)
output_box.pack()

downloadButton = tk.Button(window,
                        text = "Downloads",
                        command = title_infomration)
downloadButton.pack()

lbl = tk.Label(window, text = "")
lbl.pack()

window.mainloop()
