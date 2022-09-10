import random
import re

from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout
from os.path import exists

class MyApp(App):
# layout
# Five page app
# Page1 = player1 infomation, sumbit button
# Page2  = attakcs for player1, file, next_page button
# page3 = player2 information, sumbut buttion
# page4 = attakcs for player2, file, next_page  button
# page5 = create the simulation for character, sim button, stop button
    def database(self, child, attacks_written):
        try:
            if os.path.exists('attacks.txt') == True:
                with open('attacks.txt', 'w') as f:
                    f.write(f'{attacks_written}')
            else:
                with open('attacks.txt', 'w') as f:
                    f.write(f'{attacks_written}')
            attakcs = []
            states = []
            dodge = child['dodge'].item()
            for attakc in child['attacks'].item():
                attakcs.apppend(attakc)
            name = child['name'].item()
            try:
                for state in child['states'].item():
                    
        except Exception as error:
            print(error)

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="Submit")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        self.lbl1 = Label(text="")
        layout.add_widget(self.lbl1)
        self.lbl2 = Label(text="In moves type name of move and power of move like kiblast28. Seprate with commas")
        layout.add_widget(self.lbl2)
        self.txt1 = TextInput(text='Player 1: ', multiline=False)
        layout.add_widget(self.txt1)
        self.txt2 = TextInput(text='Moves: ', multiline=False)
        layout.add_widget(self.txt2)
        self.txt3 = TextInput(text='States: ', multiline=False)
        layout.add_widget(self.txt3)
        self.txt4 = TextInput(text='Chance of dodgeing: ', multiline=False)
        layout.add_widget(self.txt4)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "Charcter was"
        self.child = {'Name': self.txt1.text, 'Phone number' : self.txt2.text, 'Address':self.txt3.text, 'Prodcut Name':self.txt4.text, }
        attacks_written = self.txt2.text
        self.database(self.child, attacks_written)

# run app
if __name__ == "__main__":
    MyApp().run()
