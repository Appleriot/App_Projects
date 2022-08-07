import pymongo

from trycourier import Courier
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
from kivy.uix.boxlayout import BoxLayout

class MyApp(App):
# layout
    def database(self, child):
        try:
            password = "teentitan"
            client = Courier(auth_token='pk_prod_Q6QC5FAXNXM1ZPKZQDJ49JTKK97V')
            myclient = pymongo.MongoClient(
                "mongodb://Doakes:pokemonmaster@cluster0-shard-00-00.svxda.mongodb.net:27017,cluster0-shard-00-01.svxda.mongodb.net:27017,cluster0-shard-00-02.svxda.mongodb.net:27017/?ssl=true&replicaSet=atlas-93gp11-shard-0&authSource=admin&retryWrites=true&w=majority")
            mydb = myclient.test
            mycollection = mydb["customors"]
            dicts = child
            x = mycollection.insert_one(dicts)
            myclient.close()
            resp = client.send(
                event="courier-quickstart",
                recipient="ditaeviondoakes@gmail.com",
                data={
                    "infromation": f'{child}'
                },
                profile={
                    "email": "ditaeviondoakes@gmail.com"
                }
            )
        except Exception as error:
            print(error)

    def build(self):
        layout = BoxLayout(padding=10, orientation='vertical')
        btn1 = Button(text="Submit")
        btn1.bind(on_press=self.buttonClicked)
        layout.add_widget(btn1)
        self.lbl1 = Label(text=" ")
        layout.add_widget(self.lbl1)
        self.txt1 = TextInput(text='Name: ', multiline=False)
        layout.add_widget(self.txt1)
        self.txt2 = TextInput(text='Phone number: ', multiline=False)
        layout.add_widget(self.txt2)
        self.txt3 = TextInput(text='Address: ', multiline=False)
        layout.add_widget(self.txt3)
        self.txt4 = TextInput(text='Product Name: ', multiline=False)
        layout.add_widget(self.txt4)
        self.txt5 = TextInput(text='Date: ', multiline=False)
        layout.add_widget(self.txt5)
        return layout

# button click function
    def buttonClicked(self,btn):
        self.lbl1.text = "The information was sent."
        self.child = {'Name': self.txt1.text, 'Phone number' : self.txt2.text, 'Address':self.txt3.text, 'Prodcut Name':self.txt4.text, 'Date':self.txt5.text}
        self.database(self.child)

# run app
if __name__ == "__main__":
    MyApp().run()