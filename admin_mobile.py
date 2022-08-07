import pymongo

from trycourier import Courier
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
# layout
    def database(self):
        try:
            myclient = pymongo.MongoClient(
                "mongodb://Doakes:pokemonmaster@cluster0-shard-00-00.svxda.mongodb.net:27017,cluster0-shard-00-01.svxda.mongodb.net:27017,cluster0-shard-00-02.svxda.mongodb.net:27017/?ssl=true&replicaSet=atlas-93gp11-shard-0&authSource=admin&retryWrites=true&w=majority")
            mydb = myclient.test
            mycollection = mydb["customors"]
            for z in mycollection.find({}, {"_id": 0, "Name": -1, "Phone number": -1, "Address": -1, "Prodcut Name": -1,
                                            "Date": -1}):
                self.lbl1.text = f"{z}"
        except Exception as error:
            self.lbl1.text = "A error has happen."

    def delte(self):
        try:
            myclient = pymongo.MongoClient("mongodb://localhost:27017/")
            mydb = myclient["mydatabase"]
            mycollection = mydb["customors"]
            for z in mycollection.find({}, {"_id": 0}):
                mycollection.delete_one(z)
        except Exception as error:
            self.lbl1.text = "A error has happen"

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="Find")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        btn2 = Button(text="Remove Person")
        btn2.bind(on_press=self.button2Clicked)
        layout.add_widget(btn2)
        self.lbl1 = Label(text=" ")
        layout.add_widget(self.lbl1)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "The information was sent."
        self.database()
    def button2Clicked(self, btn):
        self.delte()
# run app
if __name__ == "__main__":
    MyApp().run()
