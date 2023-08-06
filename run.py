import requests
from tkinter import *
class NewsApp:
    def __init__(self):
        self.data = requests.get('https://newsapi.org/v2/top-headlines?country=in&apiKey=0b5f016413dd45cdb800cb781669752c').json()

        self.load_gui()

        self.load_news_item(1)




    def load_gui(self):
        self.root=Tk()
        self.root.geometry('350x600')
        self.root.resizable(0,0)
        self.root.configure(background='black')


    def clear(self):
        for i in self.root.pack_slaves():
            i.destroy()
    def load_news_item(self,index):
        self.clear()
        heading = Label(self.root,text=self.data['articles'][index]['title'],bg='black',fg='white',wraplength=350,justify='center')
        heading.pack(pady=(10,20))
        heading.config(font=('verdana',15))
        self.root.mainloop()




obj = NewsApp()